"""A walrus pattern looks like d := datetime(year=2020, month=m). It matches 
only if its sub-pattern also matches. It binds whatever the sub-pattern match 
does, and also binds the named variable to the entire object.
"""

# TODO
# match group_shapes():
#     case [], [point := Point(x, y), *other]:
#         print(f"Got {point} in the second group")
#         process_coordinates(x, y)
#         ...
