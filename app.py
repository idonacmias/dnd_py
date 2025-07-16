import creture
import dungen
from sys import exit

class Main:
    def __init__(self):
        print('welcom to dnd simulatore')
        self.state = Main.order_state()
        self.main_loop()

    @staticmethod
    def order_state() -> dict:
        players = Main.create_all_player()
        dungen = Main.create_dungen()
        state = {'players' : players,
                'dungen' : dungen}
        
        return state

    @staticmethod
    def create_all_player() -> dict:
        new_input = ''
        while not new_input.isnumeric():
            print('input must be a number')
            new_input = input('how many player are you?')
        
        new_input = int(new_input)
        players = {f'player_{i}' : Main.create_new_player() for i in range(new_input)}
        return players

    @staticmethod
    def create_new_player():
        new_input = ''
        while (new_input != 'y' and 
              new_input != 'n'):
            # new_input = input('do you want to create a random cherecter? [y,n]')
            new_input = 'n'

        if new_input == 'y':
            return Main.create_random_player()

        elif new_input == 'n':
            return Main.create_chosen_player()

    def create_random_player():
        return creture.Player(atributes=(10,10,10,10,10,10),
                              race_name='elf',
                              player_class={'barbarian' : 2},
                              first_player_class='barbarian',
                              skill_pro={'history' : 1, 'athletics' : 2},
                              inventory=[{'item_type' : 'Weapone', 
                                          'name' : 'battleaxe',
                                          'amuont' : 1, 
                                          'weight' : {'lb': 4}, 
                                          'cost' : {'gp': 10}, 
                                          'dmg' : {'slashing': 8}, 
                                          'properties' : ['versatile'], 
                                          'category' : ['martial melee weapons']},
                                         
                                         {'item_type' : 'Arrmor', 
                                          'name' : 'padded', 
                                          'amuont' : 2, 
                                          'weight' : {'lb' : 8}, 
                                          'cost' : {'gp' : 5}, 
                                          'ac' : 11, 
                                          'plus_dex' : True,
                                          'max_dex' : None,
                                          'stealth_dis' : True,
                                          'min_str' : None,
                                          'category' : 'light armor'}
                                          ]
                            )
        
    @staticmethod
    def create_chosen_player():
        return creture.Player.load_from_file()

    @staticmethod
    def create_dungen():
        return dungen.Dungen()

    def main_loop(self):
        while True:
            print(self.state['dungen'].corent_room.get_discription(self.state))
            print(self.state['dungen'].corent_room.path())
            input_string = input('where would like to go?\n')
            Main.is_quiting(input_string)
            self.state['dungen'].next_room(input_string)
            
            # self.state['player_0'].level_up()
            # print(self.state['player_0'])

    def is_quiting(input_string):
        if input_string in ['quit','q', 'exit']:
            exit()


if __name__ == '__main__':
    Main()