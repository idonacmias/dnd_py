from functools import reduce

def handel_ast(ast, state):
    if 'if' in ast:
        val = handel_if(ast, state)
        
    elif 'op' in ast:
        val = handel_op(ast,state)

    elif 'leaf' in ast:
        val = handle_leaf(ast, state)

    elif '=' in ast:
        put_data(ast, state)
        val = None

    return val

def handel_if(ast, state):
    bool_val = handel_ast(ast['if'], state)
    if bool_val: 
        val = handel_ast(ast['true'], state)  

    else:
        val = handel_ast(ast['false'], state)    

    return val

def handel_op(ast,state):
    val_1 = handel_ast(ast['val_1'], state)
    opertion = ast['op']
    val_2 = handel_ast(ast['val_2'], state)
    val = eval_bin_op(val_1, opertion, val_2, state)
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
            val_1 = val_2 
        
        case '!=':
            return val_1 != val_2
        
        case '==':
            return val_1 == val_2

        case 'in':
            return val_1 in val_2


def handle_leaf(ast, state):
    val = ast['leaf']
    if isinstance(val, str):
        if val[:7] == 'state:<':
            val = get_data(val[7:], state)

        elif val[:7] == 'state:>':
            val = put_data(val[7:], state)
        
    return val

def get_data(val, state):
    object_name, *paths = val.split('<')
    my_object = state[object_name]
    my_object = reduce(getattr, 
                       paths, 
                       my_object)

    return my_object

def put_data(ast, state) -> None:
    object_path = ast['=']['object']
    val = ast['=']['val']
    val = handel_ast(val, state)
    object_name, *paths = object_path.split('>')
    my_object = state[object_name]
    my_object = reduce(getattr, 
                       paths[:1], 
                       my_object)
    
    setattr(my_object, paths[-1], val)

