from dataclasses import dataclass, field
from creture import Creture
from atribute import AtributeSet, Atribute
from skill import SkillSet
from hp import Hp
from data import all_skills, proficiency

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

    def __init__(self, skill_pro:dict, player_class:dict, **arg):
        super().__init__(**arg)  
        self.skill_pro = skill_pro
        self.player_class = player_class
        self.death_saving_throw_succsess : int = 0
        self.death_saving_throw_failers : int = 0
        self.proficiency_bonuse = self.culculate_proficiency_bonuse()
        self.inventory = dict()

    @property
    def skills(self):
        skills = []
        for skill_data in all_skills:
            try:
                pro_level = self.skill_pro[skill_data.name]
            
            except KeyError:
                pro_level = 0

            skills.append((*skill_data, pro_level))
        
        skills = SkillSet(self, *skills)

        return skills
    
    @property
    def level(self):
        return sum([level for level in self.player_class.values()])

    def culculate_proficiency_bonuse(self):
        return proficiency[self.level - 1]

    def __str__(self):
        creture_str = super().__str__()  
        player_str = [str(self.skills), 
                      f'proficiency_bonuse: {self.proficiency_bonuse}',
                      f'\nlevel\n{self.level}',
                      '\nclass\n' + '\n'.join([f'{name} : {level}' for name, level in self.player_class.items()]),
                      f'\ndeath saving throw {self.death_saving_throw_failers}, {self.death_saving_throw_succsess}',
                      f'\ninventory:\n{"backlash_n".join(self.inventory)}'.replace('backlash_n', '\n'),
                      f'conditions: {self.conditions}']

        player_str = '\n'.join(player_str)
        string = creture_str + '\n\n' + player_str
        return string

    def roll_death_save(self):
        score = roll(20)
        if score == 1:
            self.death_saving_throw_failers += 2

        elif score == 20:
            self.death_saving_throw_succsess += 2
        
        elif score <= 10:
            self.death_saving_throw_failers += 1
        
        elif score > 10:
            self.death_saving_throw_succsess += 1
        
        if self.death_saving_throw_succsess >= 3: 
            self.death_saving_throw_succsess = 0    
            self.death_saving_throw_failers = 0    
            self.condition.append('stable')        

    def level_up(self):
        #add level up feature here
        # choose_class(1)#1 is how meny level in the class
        self.hp.level_up(8) #temp dice, need to be cahnge by class
        self.long_rest()



if __name__ == '__main__':
    player = Player(hit_dice={'8' : 2},
                    speed=30,
                    atributes=AtributeSet(Atribute(20),
                                          Atribute(10),
                                          Atribute(10),
                                          Atribute(10),
                                          Atribute(10),
                                          Atribute(10)),
                    saving_throw_pro=('strength', 'dexterity'),
                    skill_pro={'history' : 1, 'athletics' : 2},
                    player_class={'wizard' : 2, 'monk' : 3})
   
    # player.atributes.strength.value += 10
    # player.atributes.wisdom.value += 10
    # player.death_saving_throw_succsess += 1


    player.inventory.update({'somthing_else' : 1})
    
    print(player)
    # player.hp.temp_hp = 10
    player.atributes.constitution.value += 20 
    # player.long_rest()
    player.level_up()
    # print(player.temporery_hp)
    print(player)

