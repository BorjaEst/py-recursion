"""Python module containing recursion examples with PEP 622"""


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
