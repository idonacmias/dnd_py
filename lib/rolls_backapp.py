from random import randrange



def roll(dice:int) -> int:
    return randrange(1, dice)

def roll_atribute(number_of_rolled_dice:int=4, max_dice:bool=True, number_of_sum_dice:int=3, dice_roll:int=6) -> int:
    rolls = [roll(dice_roll) for _ in range(number_of_rolled_dice)]
    rolls.sort(reverse=max_dice)
    atribute = sum(rolls[:number_of_sum_dice])
    return atribute

def roll_pool(pool:list) -> int:
    rolls = 0
    for dice in pool:
        rolls += roll(dice)

    return rolls
