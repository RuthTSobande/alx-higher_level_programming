#!/usr/bin/python3
def remove_char_at(my_str, n):
    if 0 <= n < len(my_str):
        return my_str[:n] + my_str[n+1:]
    else:
        return my_str
