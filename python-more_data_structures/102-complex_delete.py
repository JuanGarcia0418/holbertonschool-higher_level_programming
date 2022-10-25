#!/usr/bin/python3
def complex_delete(my_dict, value):
    key_del = []
    for key in my_dict:
        if my_dict[key] == value:
            key_del.append(key)
    for key in key_del:
        del my_dict[key]
    return my_dict
