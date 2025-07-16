from dataclasses import dataclass, field

import sys
from pathlib import Path
filepath = Path(__file__)
filepath = filepath.parent.parent
sys.path.insert(0, str(filepath))
from lib import roll




class Atribute:
    def __init__(self, 
                 value: int=None,
                 number_of_rolled_dice: int = 4,
                 max_dice: bool = True,
                 number_of_sum_dice: int = 3,
                 dice_roll: int = 6
                ):

        if not value: 
            value = Atribute.roll_atribute(number_of_rolled_dice,
                                           max_dice,
                                           number_of_sum_dice,
                                           dice_roll
                                          )

        self._value = value
        self.value = self._value

    @property
    def mod(self) -> int:
        mod = (self.value - 10) // 2
        return mod
    
    def __str__(self) -> str:
        return f'{self.value} : {self.mod}'

    def __add__(self, num: int):
        self.value += num

    def ability_score_improvment(self, num):
        self._value += num
        self.value += num

    @staticmethod
    def roll_atribute(
        number_of_rolled_dice: int,
        max_dice: bool,
        number_of_sum_dice: int,
        dice_roll: int,
    ) -> int:

        rolls = [roll(dice_roll) for _ in range(number_of_rolled_dice)]
        rolls.sort(reverse=max_dice)
        atribute = sum(rolls[:number_of_sum_dice])
        return atribute




@dataclass
class AtributeSet:
    strength : Atribute = field(default_factory=Atribute) 
    dexterity : Atribute = field(default_factory=Atribute)
    constitution : Atribute = field(default_factory=Atribute)
    wisdom : Atribute = field(default_factory=Atribute)     
    intelligence : Atribute = field(default_factory=Atribute)
    charisma : Atribute = field(default_factory=Atribute)
    
    def __str__(self) -> str:
        strings = [f'strength : {self.strength.value}, {self.strength.mod}',
                   f'dexterity : {self.dexterity.value}, {self.dexterity.mod}',
                   f'constitution : {self.constitution.value}, {self.constitution.mod}',
                   f'wisdom : {self.wisdom.value}, {self.wisdom.mod}',
                   f'intelligence : {self.intelligence.value}, {self.intelligence.mod}',
                   f'charisma : {self.charisma.value}, {self.charisma.mod}']
       
        return '\n'.join(strings)

    def __iter__(self) -> iter:
        return iter((self.strength.mod,
                     self.dexterity.mod,
                     self.constitution.mod,
                     self.wisdom.mod,
                     self.intelligence.mod,
                     self.charisma.mod))

    def _iter_true_value(self)-> iter:
        return iter((self.strength._value,
                     self.dexterity._value,
                     self.constitution._value,
                     self.wisdom._value,
                     self.intelligence._value,
                     self.charisma._value))
    
    def order_data_to_saved(self):
        return tuple(self._iter_true_value())
