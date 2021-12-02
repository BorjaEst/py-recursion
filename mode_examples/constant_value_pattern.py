"""A constant value pattern works like the literal but for certain named
constants. Note that it must be a qualified (dotted) name, given the possible
ambiguity with a capture pattern. It looks like Color.RED and only matches 
values equal to the corresponding value. It never binds.
"""

class State(object):
    A = "a"
    B = "b"


# State machine
def change_state():
    new_sate = input("Introduce new state...")
    match new_sate:
        case State.A: state_a()
        case _: bad_sate()

def state_a():
    print("I am in state 'a'")
    change_state()

def bad_sate():
    print(f"Unknown state")
