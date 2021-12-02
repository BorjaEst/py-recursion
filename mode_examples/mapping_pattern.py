"""A mapping pattern looks like {"user": u, "emails": [*es]}. It matches 
mappings with at least the set of provided keys, and if all the sub-patterns
match their corresponding values. It binds whatever the sub-patterns 
bind while matching with the values corresponding to the keys. Adding **rest
at the end of the pattern to capture extra items is allowed.
"""


def process_config(config):
    match config:
        case {"a": a, **rest}:
            print(f"Configure a: {a}")
            process_config(rest)
        case {}:
            print(f"Configuration end")
        case _:
            raise ValueError("Not valid config")

def process_config(config):
    match config:
        case {"a": a, **rest}:
            print(f"Configure a: {a}")
            process_config(rest)
        case {key: val, **rest}: # TODO not sure how to solve this
            raise ValueError(f"Not a suitable key {key}")
        case {}:
            print(f"Configuration end")
        case _:
            raise ValueError("Not valid config")
