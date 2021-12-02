"""An OR pattern looks like [*x] | {"elems": [*x]}. It matches if any 
of its sub-patterns match. It uses the binding for the leftmost pattern 
that matched.
"""

class A():
    __match_args__ = ("state",)                                                                         
    def __init__(self, state):
        self.state = state


def process_class(instance):
    match instance:
        case A('a') | A('b'): process_as_ab(instance)
        case _:
            raise ValueError("Not valid instance")

def process_as_ab(instance):
    print(f"instance 'ab': {instance}")
