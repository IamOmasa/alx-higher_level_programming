#!/usr/bin/python3
"""a function that divides element by element 2 lists"""


def list_division(my_list_1, my_list_2, list_length):
    result_lst = []
    for i in range(list_length):
        result = 0
        try:
            if i >= len(my_list_1[i]) or i >= len(my_list_2[i]):
                raise IndexError("out of range")
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_lst.append(result)

    return result_lst
