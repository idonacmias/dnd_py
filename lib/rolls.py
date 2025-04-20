from random import randrange

def roll(dice:int) -> int:
    return randrange(1, dice)

def roll_atribute() -> int:
    rolls = [roll(6) for _ in range(4)]
    atribute = sum(rolls) - min(rolls)
    return atribute

def roll_pool(pool:dict) -> int:
    rolls = 0
    for dice, amuont in pool.items():
            for _ in range(amuont):
                rolls += roll(int(dice))

    return rolls
