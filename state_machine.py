"""Python module containing recursion examples with PEP 622"""


class States(object):
    A = "a" # Constant for state 'a'
    B = "b" # Constant for state 'b'


# State machine
def init(data):
    state_a(data) # Initial state is 'a'

def change_state(data):
    new_sate = input("Introduce new state...")
    match new_sate:
        case States.A: state_a(data)
        case States.B: state_b(data)
        case _: terminate()

def state_a(data):
    print("I am in state 'a'")
    print(f"State data = {data}")
    change_state()

def state_b(data):
    print("I am in state 'b'")
    print(f"State data = {data}")
    change_state()

def terminate():
    print(f"Ending state machine")
