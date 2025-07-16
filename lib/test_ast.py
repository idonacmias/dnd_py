import pytest
from .ast import handel_ast

@pytest.fixture
def state():
    state = {'name' : 'bob',
            'age' : 10,
            'roll' : 'wizard'}

    return state

def test_handel_ast_leaf(state):
    ast = {'leaf' : 'assertion'}
    assert handel_ast(ast, state) == 'assertion'

def test_handel_ast_equivalent(state):
    ast = {'val_1' : {'leaf' : 10},
            'op' : '==',
            'val_2' : {'leaf' : 10} 
             }
    assert handel_ast(ast, state)

def test_handel_ast_add(state):
    ast = {'val_1' : {'leaf' : 10},
            'op' : '+',
            'val_2' : {'leaf' : 20} 
           }
    assert handel_ast(ast, state) == 30

def test_handel_ast_gt(state):
    ast = {'val_1' : {'leaf' : 10},
            'op' : '>',
            'val_2' : {'leaf' : 20} 
           }
    assert not handel_ast(ast, state)

def test_handel_ast_st(state):
    ast = {'val_1' : {'leaf' : 10},
            'op' : '<',
            'val_2' : {'leaf' : 20} 
           }
    assert handel_ast(ast, state)


def test_handel_ast_add_str(state):
    ast = {'val_1' : {'leaf' : '10'},
            'op' : '+',
            'val_2' : {'leaf' : '20'} 
           }
    assert handel_ast(ast, state) == '1020'

def test_handel_ast_if_statment(state):
    ast =  {'if' :{'val_1' : {'leaf' : 10},
                    'op' : '==',
                    'val_2' : {'leaf' : 10} 
                   },
            'true' : {'leaf' : True},             
            'false' : {'leaf' : False}             
            }
    assert handel_ast(ast, state)

def test_handel_ast_if_statment_str_res(state):
    ast =  {'if' : {'val_1' : {'leaf' : 10},
                    'op' : '==',
                    'val_2' : {'leaf' : 10} 
                   },
            'true' : {'val_1' : {'leaf' : '10'},
                       'op' : '+',
                       'val_2' : {'leaf' : '20'} 
                       },             
            'false' : {'leaf' : False}             
            }
    assert handel_ast(ast, state) == '1020'

def test_handel_ast_change_state(state):
    ast = {'val_1' : {'leaf' : 'state:>name'},
            'op' : '=',
            'val_2' : {'leaf' : 'tom'}
           }
    handel_ast(ast, state)    
    assert state['name'] == 'tom'

def test_handel_ast_get_state(state):
    ast = {'leaf' : 'state:<name'}
    assert handel_ast(ast, state) == 'bob'


