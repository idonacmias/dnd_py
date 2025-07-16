import sys
from pathlib import Path
filepath = Path(__file__)
filepath = filepath.parent.parent
sys.path.insert(0, str(filepath))
from lib import roll, roll_pool




class Hp:
    def __init__(self, player, load=None):
        self.player = player
        if load:
            self.true_max_hp = load['true_max_hp']
            self.temp_max_hp = load['temp_max_hp']   
            self.temp_hp = load['temp_hp'] 
            self.unused_hit_dice = load['unused_hit_dice'] 

        else:
            self.true_max_hp = self.culculate_first_hp()
            self.temp_max_hp = self.true_max_hp
            self.temp_hp = self.true_max_hp
            self.unused_hit_dice = self.player.hit_dice
        

    def first_roll(self, dice=0) -> int:
        res = roll_pool(self.player.hit_dice[1:])  
        res += self.player.hit_dice[0]

        return res

    def culculate_first_hp(self, misc=0) -> int:
        rolled_hp = self.first_roll()
        max_hp = (len(self.player.hit_dice) * self.player.atributes.constitution.mod) 
        max_hp += rolled_hp
        max_hp += misc
        return max_hp
    
    def __str__(self) -> str:
        strings = [f'ture_max_hp: {self.true_max_hp}',
                   f'temp_max_hp: {self.temp_max_hp}',
                   f'temp_hp: {self.temp_hp}', 
                   f'unused_hit_dice: {self.unused_hit_dice}']
        return '\n'.join(strings)

##########################data functionality##########################

    def order_data_to_saved(self):
        hp = {'true_max_hp' : self.true_max_hp, 
              'temp_max_hp' : self.temp_max_hp, 
              'temp_hp' : self.temp_hp, 
              'unused_hit_dice' : self.unused_hit_dice}
        return hp

##########################game functionality##########################


    def long_rest(self)-> None:
        self.temp_hp = self.temp_max_hp
        self.unused_hit_dice = self.player.hit_dice

    def short_rest(self, hit_dice:dict)-> None:
        if self.is_equle_or_under(hit_dice):
            self.add_hp(hit_dice)
            self.unused_hit_dice = self.subtract_hit_dice(hit_dice)

    def is_equle_or_under(self, hit_dice) -> bool:
        for dice in set(hit_dice):
            if hit_dice.count(dice) > self.unused_hit_dice.count(dice):
                print('\n\ninvalid hit dice pool\n\n')
                return False

        return True

    def add_hp(self, dice_pool={}, misc=0) -> None:
        #shuled not update dice_pool while dice_pool empty!!!
        hp_regenerate = roll_pool(dice_pool) + misc
        self.temp_hp += hp_regenerate
        if self.temp_hp > self.temp_max_hp: 
            self.temp_hp = self.temp_max_hp

    def subtract_hit_dice(self, dice_pool: dict) -> list:
        return [dice for dice in self.unused_hit_dice if dice not in dice_pool or dice_pool.remove(dice)]

    def level_up(self, dice) -> None:
        new_roll = roll(dice)
        added_hp = new_roll + self.player.atributes.constitution.mod
        self.true_max_hp += added_hp
        self.temp_max_hp += added_hp
        self.unused_hit_dice = self.player.hit_dice
        self.player.hit_dice.append(dice)

