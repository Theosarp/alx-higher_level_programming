#!/usr/bin/python3

# Does exactly the same as a given Python bytecode

def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                res += (a**b)/i
        except Exception:
            res = b + a
            break
    return (res)
