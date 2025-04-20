from dataclasses import dataclass, field
from creture import Creture, AtributeSet, Atribute
from data import all_skills, proficiency

''' 
death throws check
level up
inventory
items
insperetion (bool)
pleyer_class
'''


@dataclass
class Player(Creture):
    skill_pro : dict
    player_class : dict
    death_saving_throw_succsess : int = 0
    death_saving_throw_failers : int = 0

    @property
    def inventory(self):
        return {'somthing': 'test'}

    @property
    def skills(self):
        skills = []
        for skill_data in all_skills:
            try:
                pro_level = self.skill_pro[skill_data.name]
            
            except KeyError:
                pro_level = 0

            skills.append((*skill_data, pro_level))
        
        skills = SkillSet(self, *skills)

        return skills
    
    @property
    def level(self):
        return sum([level for level in self.player_class.values()])

    @property
    def proficiency_bonuse(self):
        return proficiency[self.level - 1]

    def __str__(self):
        creture_str = super().__str__()  
        player_str = [str(self.skills), 
                      f'proficiency_bonuse: {self.proficiency_bonuse}',
                      f'\nlevel\n{self.level}',
                      '\nclass\n' + '\n'.join([f'{name} : {level}' for name, level in self.player_class.items()]),
                      f'\ndeath saving throw {self.death_saving_throw_failers}, {self.death_saving_throw_succsess}',
                      f'\ninventory:\n{"backlash_n".join(self.inventory)}'.replace('backlash_n', '\n')]

        player_str = '\n'.join(player_str)
        string = creture_str + '\n\n' + player_str
        return string


@dataclass
class Skill:
    player : Player
    name : str
    atribute : str
    pro_level : int
 
    @property
    def mod(self) -> int:
        atr_mod = getattr(player.atributes, self.atribute).mod
        pro_bonus = self.player.proficiency_bonuse
        return atr_mod + (self.pro_level * pro_bonus)

    def __str__(self):
        string = f'{self.name}: {self.atribute} -> {self.mod}'
        return string


@dataclass
class SkillSet:
    def __init__(self, player, *arg):
        for skill in arg:
            setattr(self, skill[0], Skill(player, *skill))

    def __str__(self):
        string = 'skills'+ '\n' + '\n'.join([str(skill) for skill in self.__dict__.values()])
        return string


if __name__ == '__main__':
    player = Player(hit_dice={'8' : 2},
                    speed=30,
                    atributes=AtributeSet(Atribute(20),
                                          Atribute(10),
                                          Atribute(10),
                                          Atribute(10),
                                          Atribute(10),
                                          Atribute(10)),
                    saving_throw_pro=('strength', 'dexterity'),
                    skill_pro={'history' : 1, 'athletics' : 2},
                    player_class={'wizard' : 2, 'monk' : 1})
   
    player.atributes.strength.value += 10
    player.atributes.wisdom.value += 10
    player.death_saving_throw_succsess += 1


    player.inventory.update({'somthing_else' : 1})
    print(player)

