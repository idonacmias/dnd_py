class Inventory():
    def __init__(self, *items):
        self.inventory_set = {}
        self.weapone_set = {}
        self.item_set = {}
        self.potion_set = {}
        self.arrmor_set = {}
        for item in items:
            self.add_new_item(item)

    def add_new_item(self, item: dict):
        set_dict = self.item_sorter(item)
        self.add_item_to_set(set_dict, item)
        self.inventory_set.update(**set_dict)

    def item_sorter(self, item: dict) -> dict:
            item_type = item['item_type']
            if item_type == 'Item':
                return self.item_set
        
            elif item_type == 'Weapone':
                return self.weapone_set

            elif item_type == 'Potion':
                return self.potion_set

            elif item_type == 'Arrmor':
                return self.arrmor_set

            else:
                print(f'not a valid category: {item_type}')

    def add_item_to_set(self, set_dict, item : dict) -> dict:
        try:
            set_dict[item['name']]['amuont'] += 1

        except KeyError:
            set_dict.update({item['name'] : item})

    def __str__(self):
        header = 'Inventory:\n'
        content = '\n'.join([Inventory.dict_to_string(item) for item in self.inventory_set.values()])
        return header + content

    @staticmethod
    def dict_to_string(my_dict: dict) -> str:
        string = [f'{key}: {val}' for key, val in my_dict.items()]
        return '\n' +'\n'.join(string)
    
    def order_data_to_saved(self):
        return list(self.inventory_set.values())
