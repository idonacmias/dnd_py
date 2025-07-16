import json
from lib import ast


class Dungen:
    def __init__(self, name: str='tutorial', room: str='start'):
        self.name = name
        self.dungen = Dungen.load(name)
        self.corent_room = self.dungen[room]

    def __str__(self):
        return str(self.dungen['room_0'])

    def next_room(self, name: str | int) -> None:
        if name.isnumeric():
            name = self.corent_room.path(name)
            print(f'next room name: {name} ')
        
        if name in self.dungen:
            self.corent_room = self.dungen[name]

        else:
            print(f'{name} is not a valid room')
   
    @staticmethod
    def load(name) -> dict:
        dungen = {}
        with open(f'files/dungens/{name}.json') as f:
            data = json.load(f)
            for key, val in data.items():
                room = Room(key, **val)
                dungen.update({key : room})
        
        return dungen

class Room:
    def __init__(self,
                 name : str,
                 # monsters : list,
                 # objects : list,
                 discription_options : str,
                 conected_path : list):
                                              
        self.name = name
        self.discription_options = discription_options
        # self.monsters = monsters 
        # self.objects = objects 
        self.conected_path = conected_path

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'{self.name} : {self.conected_path}'

    def path(self, num: str='0') -> str:
        string = ''
        for i, room_name in enumerate(self.conected_path, 1):
            if num.isnumeric() and int(num) == i:
                return room_name

            string += f'{i}) {room_name}\n' 

        return string

    def get_discription(self, state=None):
        if isinstance(self.discription_options, str):
            string = self.discription_options

        elif (isinstance(self.discription_options, dict) and
              isinstance(state, dict)):
            
            string = ast(self.discription_options, state)

        return string

    

