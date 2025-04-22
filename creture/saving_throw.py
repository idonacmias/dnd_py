from dataclasses import dataclass, field

@dataclass
class SavingThrow:
    strength : int
    dexterity : int
    constitution : int
    wisdom : int
    intelligence :int
    charisma : int

    def __str__(self):
        strings = [f'strength : {self.strength}',
                   f'dexterity : {self.dexterity}',
                   f'constitution : {self.constitution}',
                   f'wisdom : {self.wisdom}',
                   f'intelligence : {self.intelligence}',
                   f'charisma : {self.charisma}']
       
        return '\n'.join(strings)

