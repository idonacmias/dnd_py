from random import randrange


def roll(dice: int) -> int:
    return randrange(1, dice)

def roll_with_adventage(dice: int=20, advantage: int=2, dis: bool=False) -> int:
    rolls = [roll(dice) for _ in advantage]
    if dis: 
        score = min(rolls)

    else: 
        score = max(rolls)

    return score 

def roll_pool(pool: list | dict, reroll_one: bool=False) -> int:
    if isinstance(pool, dict):
        pool = pool_dict_to_list(pool)
    
    rolls = 0
    for dice in pool:
        dice_roll = roll(dice)
        if reroll_one and dice_roll == 1:
            dice_roll = roll(dice)

        rolls += dice_roll

    return rolls


def pool_dict_to_list(dict_pool: dict)->list:
    list_pool = []
    for dice, amuont in dict_pool.items():
        list_pool +=  [dice] * amuont

    return list_pool