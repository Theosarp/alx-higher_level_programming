#!/usr/bin/python3

# Executes a function safely


def safe_function(fct, *args):
    try:
        num = fct(*args)
        return num
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
