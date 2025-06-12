from dataclasses import dataclass, field
from lib import roll_atribute




@dataclass
class Atribute:
    value: int = field(default_factory=roll_atribute)

    @property
    def mod(self) -> int:
        mod = (self.value - 10) // 2
        return mod
    
    def __str__(self) -> str:
        return f'{self.value} : {self.mod}'

    def __add__(self, num):
        self.value += num

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
