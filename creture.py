from dataclasses import dataclass, field
from lib import roll, roll_atribute, roll_pool

@dataclass
class Atribute:
    value: int = field(default_factory=roll_atribute)

    @property
    def mod(self):
        mod = (self.value - 10) // 2
        return mod
    
    def __str__(self):
        return f'{self.value} : {self.mod}'


@dataclass
class AtributeSet:
    strength : Atribute = field(default_factory=Atribute) 
    dexterity : Atribute = field(default_factory=Atribute)
    constitution : Atribute = field(default_factory=Atribute)
    wisdom : Atribute = field(default_factory=Atribute)     
    intelligence : Atribute = field(default_factory=Atribute)
    charisma : Atribute = field(default_factory=Atribute)

    def __str__(self):
        strings = [f'strength : {self.strength.value}, {self.strength.mod}',
                   f'dexterity : {self.dexterity.value}, {self.dexterity.mod}',
                   f'constitution : {self.constitution.value}, {self.constitution.mod}',
                   f'wisdom : {self.wisdom.value}, {self.wisdom.mod}',
                   f'intelligence : {self.intelligence.value}, {self.intelligence.mod}',
                   f'charisma : {self.charisma.value}, {self.charisma.mod}']
       
        return '\n'.join(strings)

    def __iter__(self):
        return iter((self.strength.mod,
                     self.dexterity.mod,
                     self.constitution.mod,
                     self.wisdom.mod,
                     self.intelligence.mod,
                     self.charisma.mod))


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

    
@dataclass
class Creture:
    hit_dice : dict
    speed : int
    saving_throw_pro : tuple
    atributes : AtributeSet

    @property
    def proficiency_bonuse(self):
        return 2

    @property
    def ac(self) -> int:
        ac = 10 + self.atributes.dexterity.mod 
        return ac

    @property
    def hp(self) -> int:
        #need to max the first dice roll of hp
        hp = roll_pool(self.hit_dice)
        amuont_of_hit_dice = sum([amuont for amuont in self.hit_dice.values()])
        hp += amuont_of_hit_dice * self.atributes.constitution.mod
        return hp

    @property
    def initiative(self):
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
                  f'hp: {self.hp}',
                  f'speed: {self.speed}']

        return '\n\n'.join(string)


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
