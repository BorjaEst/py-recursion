"""A capture pattern looks like x and is equivalent to an identical assignment
target: it always matches and binds the variable with the given (simple) name.
"""


# State machine (Ctrl+c to exit)
def change_state():
    new_sate = input("Introduce new state...")
    match new_sate:
        case 'a': state_a()
        case x: dynamic(x)

def state_a():
    print("I am in state 'a'")
    change_state()

def dynamic(value):
    print(f"I am in a state '{value}'")
    change_state()
