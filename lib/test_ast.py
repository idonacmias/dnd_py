import pytest
from .ast import handel_ast
from creture import Player
from dungen import Dungen 

@pytest.fixture
def state():
    state = {'players' : Player.load_from_file('test'),
             'dungen' : Dungen()}

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

# def test_handel_ast_change_state(state):
#     ast = {'val_1' : {'leaf' : 'state:>players>'},
#             'op' : '=',
#             'val_2' : {'leaf' : 'tom'}
#            }
#     handel_ast(ast, state)    
#     assert state['players'].name == 'tom'

def test_handel_ast_get_player_speed(state):
    ast = {'leaf' : 'state:<players<speed'}
    assert handel_ast(ast, state) == 30

def test_handel_ast_get_player_hp(state):
    ast = {'leaf' : 'state:<players<hp<true_max_hp'}
    assert handel_ast(ast, state) == 19

def test_handel_ast_get_corent_room_name(state):
    ast = {'leaf' : 'state:<dungen<corent_room<name'}
    assert handel_ast(ast, state) == 'start'

def test_handel_ast_put(state):
    ast = {'=' : {'object' : 'players>speed',
                  'val' : {'leaf' : 35}
                  }
          }
    handel_ast(ast, state)
    assert state['players'].speed == 35


def test_handel_ast_put(state):
    ast = {'=' : {'object' : 'players>hp>true_max_hp',
                  'val' : {'leaf' : 200}
                  }
          }

    handel_ast(ast, state)
    assert state['players'].hp.true_max_hp == 200


def test_handel_ast_add_to_inventory(state):
    ast = {'=' : {'object' : 'players>inventory>weapone_set',
                  'val' : {'leaf' : {'item_type' : 'Weapone', 
                                          'name' : 'battleaxe',
                                          'amuont' : 2, 
                                          'weight' : {'lb': 4}, 
                                          'cost' : {'gp': 10}, 
                                          'dmg' : {'slashing': 8}, 
                                          'properties' : ['versatile'], 
                                          'category' : ['martial melee weapons']},
                                         }
                  }
          }
          
    handel_ast(ast, state)
    assert state['players'].inventory.weapone_set['battleaxe']['amuont'] == 2

