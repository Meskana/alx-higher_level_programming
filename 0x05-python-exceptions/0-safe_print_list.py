#!/usr/bin/python3
# a function that prints x elements of a list.


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i, e in enumerate(my_list):
            if i >= x:
                break
            print(e, end="")
            count += 1
        print()
    except TypeError as e:
        print(e)
    return count
