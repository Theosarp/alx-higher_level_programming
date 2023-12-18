#!/usr/bin/python3

# Divides element by element 2 lists

def list_division(my_list_1, my_list_2, list_length):
   div_result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (IndexError, ValueError):
            print("out of range")
        finally:
            div_result.append(div)
    return div_result
