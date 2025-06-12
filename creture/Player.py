from .atribute import AtributeSet, Atribute
from .hp import Hp
from creture import Creture
from data import races, player_classes, proficiency

import tomllib
import tomli_w

import os

import sys
from pathlib import Path
filepath = Path(__file__)
filepath = filepath.parent.parent
sys.path.insert(0, str(filepath))
from lib import roll
# from items import ItemSet

''' 
class dictet hit dice dict
level up
inventory
items
insperetion (bool)
pleyer_class
turn
'''


class Player(Creture):

    def __init__(self, first_player_class: str, player_class: dict, race: str, **arg):
        speed, saving_throw_pro, hit_dice = Player._pre_super_clean_up(first_player_class, player_class, race)
        super().__init__(**arg, hit_dice=hit_dice ,saving_throw_pro=saving_throw_pro, speed=speed)  
        self.race = races[race]
        self.atribute_race_mod()
        self.first_player_class = first_player_class
        self.player_class = player_class
        self.death_saving_throw_succsess = 0
        self.death_saving_throw_failers = 0
        self.proficiency_bonuse = self.culculate_proficiency_bonuse()
        self.save_to_file()

    @staticmethod
    def _pre_super_clean_up(first_player_class, player_class, race):
        speed = races[race]['speed']
        saving_throw_pro = player_classes[first_player_class]['proficiencies']['saving_throw']
        hit_dice = Player.order_hit_dice(player_class, first_player_class)
        return speed, saving_throw_pro, hit_dice

    @staticmethod
    def order_hit_dice(player_class, first_player_class)->list:
        hit_dice_list = []
        for class_name, level in player_class.items():
            class_hit_dice_val = player_classes[class_name]['hit_dice']
            temp_hit_dice_list = [class_hit_dice_val] * level
            if class_name == first_player_class: 
                hit_dice_list = temp_hit_dice_list + hit_dice_list
    
            else:
                hit_dice_list += temp_hit_dice_list

        return hit_dice_list

    def atribute_race_mod(self):
        for atribute, bonus in self.race['atribute_bonus'].items():
            player_atribute = getattr(self.atributes, atribute)
            player_atribute += bonus

    def culculate_proficiency_bonuse(self) -> int:
        return proficiency[self.level - 1]


    @property
    def level(self) -> int:
        return sum([level for level in self.player_class.values()])


    def __str__(self) -> str:
        creture_str = super().__str__()  
        player_str = [str(self.skills), 
                      f'proficiency_bonuse: {self.proficiency_bonuse}',
                      f'\nlevel\n{self.level}',
                      '\nclass\n' + '\n'.join([f'{name} : {level}' for name, level in self.player_class.items()]),
                      f'\ndeath saving throw {self.death_saving_throw_failers}, {self.death_saving_throw_succsess}',
                      f'conditions: {self.conditions}']

        player_str = '\n'.join(player_str)
        string = creture_str + '\n\n' + player_str
        return string

    def roll_death_save(self) -> None:
        score = roll(20)
        if score == 1:
            self.death_saving_throw_failers += 2

        elif score == 20:
            self.death_saving_throw_succsess += 2
        
        elif score <= 10 and score != 1:
            self.death_saving_throw_failers += 1
        
        elif score > 10 and score != 20:
            self.death_saving_throw_succsess += 1
        
        if self.death_saving_throw_succsess >= 3: 
            self.death_saving_throw_succsess = 0    
            self.death_saving_throw_failers = 0    
            self.condition.append('stable')        

    def level_up(self) -> None:
        #add level up feature here
        # choose_class(1)#1 is how meny level in the class
        self.proficiency_bonuse = self.culculate_proficiency_bonuse()
        self.hp.level_up(8) #temp dice, need to be cahnge by class
        self.long_rest()

    def save_to_file(self):
        data = self.__dict__
        # print(data)
        '''
        problamatic data:
            !atribute
            !hp
            inventory
            skills - no need
        '''
        good_data = self.__dict__.copy()
        
        atributes = good_data.pop('atributes')
        atributes = [atribute for atribute in atributes]
        good_data.update({'atributes' : atributes})

        hp = good_data.pop('hp')
        hp = hp.__dict__.copy()
        hp.pop('player')
        good_data.update({'hp' : hp})

        good_data.pop('skills')

        inventory = good_data.pop('inventory')
        for inventory_type in inventory:
            print(f'inventory_type: {inventory_type}')
            for item in inventory_type:
                # pass
                print(f'item: {item}')
        # print()
        # print(good_data)
        path = f"files/players/{123}.toml"
        with open(path, "w+b") as f:
            tomli_w.dump(good_data, f)