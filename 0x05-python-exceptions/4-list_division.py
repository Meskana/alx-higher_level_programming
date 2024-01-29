#!/usr/bin/python3
"""
a function that divides element by element 2 lists.
"""

def list_division(my_list_1, my_list_2, list_length):
    result_len = []
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]

            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
            result_len.append(result)
    except IndexError:
        print("out of range")
    finally:
        return result_len
