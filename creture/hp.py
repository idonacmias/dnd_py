import sys
from pathlib import Path
filepath = Path(__file__)
filepath = filepath.parent.parent
sys.path.insert(0, str(filepath))
from lib import roll, roll_pool




class Hp:
    #need to add a player short rest
    #need to add a bard song of rest?
    
    def __init__(self, player):
        self.player = player
        self.rolled_hp = self.roll_hp_dice()
        self.true_max_hp = self.culculate()
        self.temp_max_hp = self.true_max_hp
        self.temp_hp = self.true_max_hp
        self.unused_hit_dice = self.player.hit_dice

    def roll_hp_dice(self, dice=0):
        if not dice:
            res = roll_pool(self.player.hit_dice)

        else:
            res = roll(dice)

        return res

    def culculate(self, misc=0) -> int:
        amuont_of_hit_dice = sum([amuont for amuont in self.player.hit_dice.values()])
        max_hp = (amuont_of_hit_dice * self.player.atributes.constitution.mod) 
        max_hp += self.rolled_hp
        max_hp += misc
        return max_hp
    
    def long_rest(self):
        self.temp_hp = self.temp_max_hp
        self.unused_hit_dice = self.player.hit_dice

    def level_up(self, dice):
        new_roll = self.roll_hp_dice(dice)
        added_hp = new_roll + self.player.atributes.constitution.mod
        self.true_max_hp += added_hp
        self.temp_max_hp += added_hp
        try:
            self.player.hit_dice[str(dice)] += 1

        except KeyError:
            self.player.hit_dice.update({str(dice) : 1})


    def __str__(self):
        strings = [f'ture_max_hp: {self.true_max_hp}',
                   f'temp_max_hp: {self.temp_max_hp}',
                   f'temp_hp: {self.temp_hp}']
        return '\n'.join(strings)

