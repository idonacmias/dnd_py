import items
import creture
from sys import exit

class Main:
    def __init__(self):
        self.q_string = 'welcom to dnd simulatore'
        self.input_string = ''
        self.data = Main.order_data()
        self.main_loop()

    @staticmethod
    def order_data() -> dict:
        new_input = ''
        while not new_input.isnumeric():
            print('input must be a number')
            new_input = input('how many player are you?')
        
        new_input = int(new_input)
        return {f'player_{i}' : Main.create_new_player() for i in range(new_input)}

    def main_loop(self):
        while True:
            self.input_string = input(self.q_string + '\n')
            self.is_quiting()

    def is_quiting(self):
        if self.input_string in ['quit','q', 'exit']:
            exit()

    @staticmethod
    def create_new_player():
        new_input = ''
        while (new_input != 'y' and 
              new_input != 'n'):
            new_input = input('do you want to create a random cherecter? [y,n]')

        if new_input == 'y':
            return Main.create_random_player()

        elif new_input == 'n':
            return Main.create_chosen_player()

    @staticmethod
    def create_random_player():
        return creture.Player(#atributes=(10,10,10,10,10,10),
                              race='elf',
                              player_class={'barbarian' : 1},
                              first_player_class='barbarian',
                              skill_pro={'history' : 1, 'athletics' : 2},
                              items=[['Weapone', 'battleaxe', 1, {'lb': 4}, {'gp': 10}, {'slashing': 8}, [{'Versatile' : 10}], 'Martial Melee Weapons']])


    @staticmethod
    def create_chosen_player():
        fields = ['hit dice',
                  'speed',
                  'saving_throw_pro',
                  'skill_pro',
                  'player_class',
                  'items']

        atributes =['streanth',
                    'dexterety',
                    'constitution',
                    'wisdom',
                    'intelligence',
                    'charisma']

        atributes = tuple(int(input(f'{atribute}\n')) for atribute in atributes)
        fields = {field : input(f'{field}:\n') for field in fields}
        int(fields['hit dice'])
        int(fields['speed'])

        fields.update({'atributes' : atributes})
        print(fields)
        # int(fields[0])
        creture.Player(*fields)

if __name__ == '__main__':
    Main()