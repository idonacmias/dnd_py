from creture import Creture
from data import races, player_classes, proficiency

import json

import random 

import sys
from pathlib import Path
filepath = Path(__file__)
filepath = filepath.parent.parent
sys.path.insert(0, str(filepath))
from lib import roll
# from items import ItemSet

''' 
level up
insperetion (bool)
turn
'''


class Player(Creture):

##########################initialization##########################

    def __init__(self, 
                 first_player_class: str, 
                 player_class: dict, 
                 race_name: str=None, 
                 **arg
    ):

        if not race_name: 
            race_name = Player.choose_random_race()

        speed, saving_throw_pro, hit_dice = Player._pre_super_clean_up(first_player_class, player_class, race_name)
        super().__init__(**arg, 
                         hit_dice=hit_dice ,
                         saving_throw_pro=saving_throw_pro, 
                         speed=speed
        )

        self.race_name = race_name
        self.race = races[race_name]
        self.atribute_race_mod() #TODO: adding again apon loading 
        self.first_player_class = first_player_class
        self.player_class = player_class
        self.death_saving_throw_succsess = 0
        self.death_saving_throw_failers = 0
        self.arrmor = self.inventory.arrmor_set['padded']
        self.save_to_file()

    @staticmethod
    def choose_random_race():
        return random.choice(list(races.keys()))

    @staticmethod
    def _pre_super_clean_up(first_player_class, player_class, race_name):
        speed = races[race_name]['speed']
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

    def atribute_race_mod(self) -> None:
        for atribute, bonus in self.race['atribute_bonus'].items():
            player_atribute = getattr(self.atributes, atribute)
            player_atribute += bonus

    @property
    def level(self) -> int:
        return sum([level for level in self.player_class.values()])

    @property
    def proficiency_bonuse(self) -> int:
        return proficiency[self.level - 1]

    def __str__(self) -> str:
        creture_str = super().__str__()  
        player_str = [str(self.skills), 
                      f'\nlevel\n{self.level}',
                      '\nclass\n' + '\n'.join([f'{name} : {level}' for name, level in self.player_class.items()]),
                      f'\ndeath saving throw {self.death_saving_throw_failers}, {self.death_saving_throw_succsess}',
                      f'conditions: {self.conditions}']

        player_str = '\n'.join(player_str)
        string = creture_str + '\n\n' + player_str
        return string




##########################data functionality##########################

    def save_to_file(self):
        all_data = self.__dict__.copy()
        all_data = Player.order_data_to_saved(all_data, 'atributes')
        all_data = Player.order_data_to_saved(all_data, 'hp')
        all_data = Player.order_data_to_saved(all_data, 'inventory')
        all_data.pop('skills')#can be builed without row data
        if all_data['arrmor']: 
            all_data.pop('arrmor')

        path = f"files/players/{123}.json"
        with open(path, "w") as f:
            f.write(json.dumps(all_data))

    @staticmethod
    def order_data_to_saved(all_data: dict, key: str) -> dict:
        filed = all_data.pop(key)
        data = filed.order_data_to_saved()
        all_data.update({key : data})
        return all_data

    @staticmethod
    def load_from_file(file_name='test'):
        path = f"files/players/{file_name}.json"
        with open(path, "r") as f:
            data = json.load(f)
        
        data['atributes'] = tuple(data['atributes'])
        
        player = Player(atributes=data['atributes'],
                        race_name=data['race_name'],
                        player_class=data['player_class'],
                        first_player_class=data['first_player_class'],
                        skill_pro=data['skill_pro'],
                        inventory=data['inventory'],
                        hp=data['hp'])
        return player


##########################game functionality##########################




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

        # self.atributes.wisdom.ability_score_improvment(20)
        self.hp.level_up(8) #temp dice, need to be cahnge by class
        self.long_rest()

 
