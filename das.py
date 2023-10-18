def func(my_num):
    if my_num // 2 == 0:
        return 'zero'
    if str(my_num).endswith('5'):
        return 'five'
    if my_num % 2 != 0:
        return 'odd'

    # print(my_num % 2)



res = func(15)
print(res)
print(15/5)