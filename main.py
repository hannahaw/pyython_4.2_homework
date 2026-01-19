my_list = [0, 1, 7, 2, 4, 8]

if len(my_list) == 0:
    print(0)
else:
    sum_even = sum(my_list[::2])
    result = sum_even * my_list[-1]
    print(result)
