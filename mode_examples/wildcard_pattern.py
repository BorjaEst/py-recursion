"""The wildcard pattern is a single underscore: _. It always matches,
but does not capture any variable (which prevents interference with other
uses for _ and allows for some optimizations).
"""


# State machine
def change_state():
    new_sate = input("Introduce new state...")
    match new_sate:
        case 'a': state_a()
        case _: bad_sate()

def state_a():
    print("I am in state 'a'")
    change_state()

def bad_sate():
    print(f"Unknown state")
