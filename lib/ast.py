def handel_ast(ast, state):
    if 'if' in ast:
        bool_val = handel_ast(ast['if'], state)
        if bool_val: 
            val = handel_ast(ast['true'], state)  

        else:
            val = handel_ast(ast['false'], state)    

    elif 'op' in ast:
        val_1 = handel_ast(ast['val_1'], state)
        opertion = ast['op']
        val_2 = handel_ast(ast['val_2'], state)
        val = eval_bin_op(val_1, opertion, val_2, state)

    elif 'leaf' in ast:
        leaf = ast['leaf']
        val = handle_leaf(leaf, state)

    return val

def eval_bin_op(val_1, opertion, val_2, state) -> bool | int | str | None:
    match opertion:
        case '>=':
            return val_1 >= val_2

        case '<=':
            return val_1 <= val_2
        
        case '<':
            return val_1 < val_2
        
        case '>':
            return val_1 > val_2
        
        case '//':
            return val_1 // val_2
        
        case '/':
            return val_1 / val_2
        
        case '^':
            return val_1 ** val_2
        
        case '*':
            return val_1 * val_2
        
        case '-':
            return val_1 - val_2
        
        case '+':
            return val_1 + val_2
        
        case '=':
            state[f'{val_1}'] = val_2 
        
        case '!=':
            return val_1 != val_2
        
        case '==':
            return val_1 == val_2

        case 'in':
            return val_1 in val_2


def handle_leaf(leaf, state):
    val = leaf
    if isinstance(leaf, str):
        if leaf[:7] == 'state:<':
            val = get_data(leaf[7:], state)

        elif leaf[:7] == 'state:>':
            val = leaf[7:]
        
    return val

def get_data(leaf, state):
    return state[leaf]


