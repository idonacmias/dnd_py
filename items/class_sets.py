from .item import Item, Weapone, Potion

class AbstractSet:
    def __init__(self, *items):
        for item in items:
            setattr(self, item.name, item)

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return self

    def __next__(self):
        yield self.__dict__.values()

    def __str__(self):
        return '\n'.join([str(item) for item in self.__dict__.values()])

class WeaponeSet(AbstractSet):
    def __str__(self):
        string = 'weapones:\n'
        old_string = super().__str__()
        return string + old_string


class ItemSet(AbstractSet):
    def __str__(self):
        string = 'items:\n'
        old_string = super().__str__()
        return string + old_string


class PotionSet(AbstractSet):
    
    def __str__(self):
        string = 'potions:\n'
        old_string = super().__str__()
        return string + old_string


class Inventory(AbstractSet):
    def __init__(self, *items):
        weapone_set = []
        item_set = []
        potion_set = []

        for item in items:
            new_item = Inventory.item_factory(item)
            if type(new_item) == Weapone:
                weapone_set.append(new_item)

            elif type(new_item) == Item:
                item_set.append(new_item)

            elif type(new_item) == Potion:
                potion_set.append(new_item)

            else:
                print(f'undefine type of item: \n{item}')

        else:
            self.weapone_set = WeaponeSet(*weapone_set)
            self.item_set = ItemSet(*item_set)
            self.potion_set = PotionSet(*potion_set)

   
    @staticmethod
    def item_factory(item) -> Item|Weapone|Potion:
        if item[0] == 'Item':
            return Item(*item[1:])
    
        elif item[0] == 'Weapone':
            return Weapone(*item[1:])
        
        elif item[0] == 'Potion':
            return Potion(*item[1:])

    def __str__(self):
        string = 'items:\n'
        old_string = super().__str__()
        return string + old_string




