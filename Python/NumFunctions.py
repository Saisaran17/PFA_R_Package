def sum_numbers(num):
    if num:
        # call same function by reducing number by 1
        return num + sum_numbers(num - 1)
    else:
        return 0
def sum_square_numbers(num):
    if num:
        # call same function by reducing number by 1
        return num*num + sum_square_numbers(num - 1)
    else:
        return 0
