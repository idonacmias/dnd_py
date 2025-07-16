
def ast(data, state):
    val_1, operetor, val_2 = data['val_1'], data['operetor'], data['val_2']
    val_1 = switch_case_value(val_1, state)
    val_2 = switch_case_value(val_2, state)
    
    if isinstance(val_1, list):
        multipul_answ = [switch_case_operetor(val, operetor, val_2) for val in val_1]
        val_1 = switch_case_multipul_answ(data, multipul_answ)
    
    if switch_case_operetor(val_1, operetor, val_2):
        res = data['if']

    else:
        res = data['else']
    
    print(res)    
    return res

def switch_case_value(val, state):
    if not isinstance(val, str): 
        return val

    match val:
        case 'ast':
            return ast(val, state)

        case 'strength' | 'dexterity' | 'constitution' | 'wisdom' |'intelligence' | 'charisma':
            return get_player_atribute(val, state)

        case 'hp':
            return get_player_hp(state)


def get_player_atribute(val, state) -> list:
    players = state['players']
    players_atribute = []
    for player in players.values():
        match val:
            case 'strength': 
                player_atribute = player.atributes.streanth.mod

            case  'dexterity':
                player_atribute = player.atributes.dexterity.mod

            case  'constitution': 
                player_atribute = player.atributes.constitution.mod

            case  'wisdom':
                player_atribute = player.atributes.wisdom.mod

            case 'intelligence': 
                player_atribute = player.atributes.intelligence.mod

            case 'charisma':
                player_atribute = player.atributes.charisma.mod

        players_atribute.append(player_atribute)

    return player_atribute

def get_player_hp(state) -> list:
    players = state['players']
    hps = []
    for player in players.values():
        hps.append(player.hp.temp_hp)

    return hps

def switch_case_multipul_answ(data, multipul_answ: list) -> bool:
    match data['multipul answ']:
        case 'one fail':
            return min(multipul_answ)

        case 'one pass':
            return max(multipul_answ)

        case 'all true':
            return False not in set(multipul_answ)

        case 'all false':
            return True not in set(multipul_answ)

def switch_case_operetor(val_1: str | int,operetor: str, val_2: str | int | list) -> bool:
    match operetor:
        case '>':
            return gt(val_1, val_2)

        case '<':
            return gt(val_2, val_1)

        case '==':
            return eq(val_1, val_2)

        case '!=':
            return not eq(val_1, val_2)

        case 'in':
            return is_in(val_1, val_2)

        case _:
            print(f'operetor {operetor} is not suppordet')

def gt(val_1, val_2):
    return val_1 > val_2

def eq(val_1, val_2):
    return val_1 == val_2

def is_in(val, my_list):
    return val in my_list

if __name__ == '__main__':
    data ={'val_1' : 1, 
           'operetor' : 'in', 
           'val_2' : [2,3],
           'if' : 'if text',
           'else' : 'else text'}

    ast(data)