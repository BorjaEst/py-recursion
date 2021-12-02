"""A sequence pattern looks like [a, *rest, b] and is similar to a list 
unpacking. An important difference is that the elements nested within
it can be any kind of patterns, not just names or sequences. It matches
only sequences of appropriate length, as long as all the sub-patterns 
also match. It makes all the bindings of its sub-patterns.
"""


def sum(numbers):
    match numbers:
        case []: 
            return 0
        case [n, *rest]: 
            return n + sum(rest)

def sum(numbers, acc=0):
    match numbers:
        case []: 
            return acc
        case [n, *rest]: 
            return sum(rest, acc=acc+n)

