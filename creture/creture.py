from .hp import Hp
from .atribute import AtributeSet, Atribute
from .saving_throw import SavingThrow
from .skill import SkillSet
from data import all_skills

import sys
from pathlib import Path
filepath = Path(__file__)
filepath = filepath.parent.parent
sys.path.insert(0, str(filepath))
from items import Inventory

class Creture:
##########################initialization##########################

    def __init__(self, 
                 hit_dice: list, 
                 speed: int, 
                 saving_throw_pro: tuple, 
                 inventory: list=[], 
                 skill_pro: dict={}, 
                 atributes: AtributeSet | list | tuple=(), 
                 hp: dict | None=None,
                 arrmor: dict | None=None
    ):

        self.atributes = Creture.set_atributes(atributes)
        self.hit_dice = hit_dice 
        self.speed = speed
        self.saving_throw_pro = saving_throw_pro
        self.hp = Hp(self, load=hp)
        self.conditions = []
        self.inventory = Inventory(*inventory)
        self.skill_pro = skill_pro
        self.skills = self.create_skills()
        self.arrmor = arrmor        

    def set_atributes(atributes):
        if (Creture.is_atributes_of_type(atributes) and
            Creture.is_atributes_is_ints(atributes) and
            len(atributes) == 6):
            
            return AtributeSet(*(Atribute(atribute) for atribute in atributes))
        
        elif isinstance(atributes, AtributeSet):
            return atributes
        
        else:
            print('atribute must be from type tuple with int  or AtributeSet')

    @staticmethod
    def is_atributes_of_type(atributes) -> bool:
        return (isinstance(atributes, tuple) or
                isinstance(atributes, list)) 

    @staticmethod
    def is_atributes_is_ints(atributes) -> bool:
        for atribute in atributes:
            if not isinstance(atribute, int):
                return False

        return True 

    @property
    def proficiency_bonuse(self) -> int:
        return 2

    @property
    def initiative(self) -> int:
        return self.atributes.dexterity.mod

    @property
    def saving_throw(self) -> SavingThrow:
        saving_throw = SavingThrow(*self.atributes)
        for pro in self.saving_throw_pro:
            new_saving_throw = getattr(saving_throw, pro) + self.proficiency_bonuse
            setattr(saving_throw, pro, new_saving_throw)
        
        return saving_throw

    @property
    def ac(self):
        base_bonus = 10
        dex_bonus = self.atributes.dexterity.mod
        if self.arrmor:
            base_bonus = self.arrmor['ac']
            if not self.arrmor['plus_dex']:
                dex_bonus = 0

            elif self.arrmor['max_dex']:
                dex_bonus = min(self.atributes.dexterity.mod, self.arrmor['max_dex']) 
                    

        self._ac = base_bonus + dex_bonus 
        return self._ac 

    def create_skills(self) -> SkillSet:
        skills = SkillSet(self, *all_skills)
        for skill in self.skill_pro:
            skill = getattr(skills, skill)
            if skill.pro_level < 1:
                skill.pro_level = 1

        return skills

    def __str__(self) -> str:
        string = [f'atributes:\n{self.atributes}',
                  f'proficiency_bonuse:{self.proficiency_bonuse}',
                  f'saving_throw:\n{self.saving_throw}',
                  f'ac: {self.ac}',
                  f'hp:\n{self.hp}',
                  f'speed: {self.speed}',
                  str(self.inventory)]

        return '\n\n'.join(string)

##########################game functionality##########################

    def long_rest(self) -> None:
        self.hp.long_rest()
        self.constitutions = []
