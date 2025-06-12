from dataclasses import dataclass

@dataclass
class Item:
    name : str 
    amuont : int
    weight : int
    cost : dict

    def __str__(self) -> str:
        string = [f'{self.name}:',
                  f'amuont: {self.amuont}', 
                  f'weight: {self.weight}', 
                  f'cost: {self.cost}']
        string = '\n'.join(string)
        return string

@dataclass
class Weapone(Item):
    dmg : dict 
    properties: list
    category : str

    def __str__(self) -> str:
        old_string = super().__str__()  
        new_string = [f'dmg: {self.dmg}', 
                      f'properties: {self.properties}', 
                      f'category: {self.category}',
                      '\n']
        new_string = '\n'.join(new_string)
        return old_string + '\n' + new_string


@dataclass
class Potion(Item):
    healing : dict

    def __str__(self)->str:
        old_string = super().__str__()
        healing_string = [{f"{amuont}d{dice}\n" for amuont, dice in self.healing.items()}]
        healing_string = '\n'.join(healing_string)
        new_string = [f'healing: \n', f'{healing_string}']
        return new_string
        
    def heal(self, creture)->None:
        hp_restore = roll_pool(self.healing)
        creture.hp.temp_hp += hp_restore