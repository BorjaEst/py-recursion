"""A class pattern is similar to the above but matches attributes instead 
of keys. It looks like datetime.date(year=y, day=d). It matches instances 
of the given type, having at least the specified attributes, as long as 
the attributes match with the corresponding sub-patterns. It binds whatever 
the sub-patterns bind when matching with the values of the given attributes. 
An optional protocol also allows matching positional arguments.
"""

class A():
    __match_args__ = ("state",)                                                                         
    def __init__(self, state):
        self.state = state


def process_class(instance):
    match instance:
        case A('a'): process_as_a(instance)
        case A('b'): process_as_b(instance)
        case _:
            raise ValueError("Not valid instance")

def process_as_a(instance):
    print(f"instance 'a': {instance}")

def process_as_b(instance):
    print(f"instance 'b': {instance}")
