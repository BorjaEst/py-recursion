"""A literal pattern is useful to filter constant values in a structure. 
It looks like a Python literal (including some values like True, False 
and None). It only matches objects equal to the literal, and never binds.
"""


# State machine
def change_state():
    new_sate = input("Introduce new state...")
    match new_sate:
        case 'a': state_a()
        case 'b': state_b()

def state_a():
    print("I am in state 'a'")
    change_state()

def state_b():
    print("I am in state 'b'")
    change_state()
