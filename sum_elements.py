"""Python module containing recursion examples with PEP 622"""


def sum(numbers, acc=0):
    match numbers:
        case [n, *rest]: 
            return sum(rest, acc=acc+n)
        case []: 
            return acc
