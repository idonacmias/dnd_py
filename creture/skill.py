from dataclasses import dataclass


@dataclass
class Skill:
    player : None
    name : str
    atribute : str
    pro_level : int
 
    @property
    def mod(self) -> int:
        atr_mod = getattr(self.player.atributes, self.atribute).mod
        pro_bonus = self.player.proficiency_bonuse
        return atr_mod + (self.pro_level * pro_bonus)

    def __str__(self) -> str:
        string = f'{self.name}: {self.atribute} -> {self.mod}'
        return string


@dataclass
class SkillSet:
    def __init__(self, player, *skills):
        for skill in skills:
            setattr(self, skill[0], Skill(player, *skill))

    def __str__(self) -> str:
        string = 'skills'+ '\n' + '\n'.join([str(skill) for skill in self.__dict__.values()])
        return string
