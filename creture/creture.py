from hp import Hp
from atribute import AtributeSet, Atribute
from saving_throw import SavingThrow

import sys
from pathlib import Path
filepath = Path(__file__)
filepath = filepath.parent.parent
sys.path.insert(0, str(filepath))
from lib import roll, roll_atribute, roll_pool


class Creture:

    def __init__(self, hit_dice:dict, speed:int, saving_throw_pro:tuple, atributes=AtributeSet):
        self.hit_dice = hit_dice 
        self.speed = speed
        self.saving_throw_pro = saving_throw_pro
        self.atributes = atributes
        self.hp = Hp(self)
        self.conditions = []
        self.proficiency_bonuse = 2
        self.ac = 10 + self.atributes.dexterity.mod 

    
    @property
    def initiative(self) -> int:
        return self.atributes.dexterity.mod

    @property
    def saving_throw(self) -> dict:
        saving_throw = SavingThrow(*self.atributes)
        for pro in self.saving_throw_pro:
            new_saving_throw = getattr(saving_throw, pro) + self.proficiency_bonuse
            setattr(saving_throw, pro, new_saving_throw)
        
        return saving_throw

    def __str__(self):
        string = [f'atributes:\n{self.atributes}',
                  f'saving_throw:\n{self.saving_throw}',
                  f'ac: {self.ac}',
                  f'hp:\n{self.hp}',
                  f'speed: {self.speed}']

        return '\n\n'.join(string)

    def long_rest(self):
        self.hp.long_rest()
        self.constitutions = []




if __name__ == '__main__':
    creture = Creture(hit_dice={'8' : 2},
                      speed=30,
                      atributes=AtributeSet(Atribute(20),
                                            Atribute(10),
                                            Atribute(10),
                                            Atribute(10),
                                            Atribute(10),
                                            Atribute(10)),
                      saving_throw_pro=('strength', 'dexterity'))
    print(creture)
