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
from lib import roll, roll_atribute, roll_pool
from items import Inventory

class Creture:

    def __init__(self, hit_dice: list, speed: int, saving_throw_pro: tuple, items: list, skill_pro: dict={}, atributes: tuple=()):
        self.atributes = Creture.set_atributes(atributes)
        self.hit_dice = hit_dice 
        self.speed = speed
        self.saving_throw_pro = saving_throw_pro
        self.hp = Hp(self)
        self.conditions = []
        self.proficiency_bonuse = 2
        self.ac = 10 + self.atributes.dexterity.mod 
        self.inventory = Creture.create_inventory(items)
        self.skill_pro = skill_pro
        self.skills = self.create_skills()
        
    def set_atributes(atributes):
        if (type(atributes) == tuple and
            int == type(atribute)for atribute in atributes):
            return AtributeSet(*(Atribute(atribute) for atribute in atributes))
        
        elif type(atributes) == AtributeSet:
            return atributes
        
        else:
            print('atribute must be from type tuple with int  or AtributeSet')

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

    @staticmethod
    def create_inventory(items) -> Inventory:
        items_set = Inventory(*items) 
        return items_set

    def create_skills(self) -> SkillSet:
        skills = SkillSet(self, *all_skills)
        for skill in self.skill_pro:
            skill = getattr(skills, skill)
            if skill.pro_level < 1: skill.pro_level = 1

        return skills

    def __str__(self) -> str:
        string = [f'atributes:\n{self.atributes}',
                  f'saving_throw:\n{self.saving_throw}',
                  f'ac: {self.ac}',
                  f'hp:\n{self.hp}',
                  f'speed: {self.speed}',
                  str(self.inventory)]

        return '\n\n'.join(string)

    def long_rest(self) -> None:
        self.hp.long_rest()
        self.constitutions = []


if __name__ == '__main__':
    print('not warking du to import reletive path')
    creture = Creture(hit_dice=[8, 8],
                      speed=30,
                      atributes=(20,10,10,10,10,10),
                      saving_throw_pro=('strength', 'dexterity'),
                      items=[['Item', 'potion', 1, 1, 1],['Weapone', 'club', 1, 2, {'sp' : 1}, {'bludgeoning' : 4}, ['light'], 'simple melee weapon']])
    print(creture)
    print(creture.inventory.weapone_set)