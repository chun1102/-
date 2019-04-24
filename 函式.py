# def add_x_and_y(x, y=4):
#     """
#
#     :param x:
#     :param y:
#     :return:
#     """
#     sum_num = x + y
#     return sum_num
#
# a = 10
# b = 7
# sum = add_x_and_y(a, b)
# print(sum)
#
# c = add_x_and_y(a)
# print(c)





def add_x_and_multi_y(x, *y):
    """

    :param x: eg. 8
    :param y:
    :return:
    """
    sum_num = x + sum(y)
    return sum_num

z = 7
x = 6
c = 9
v = 44
b = 65
sum1 = add_x_and_multi_y(z, x, c, v, b)
print(sum1)


def add_x_and_y_return_multi_value(x, y):
    sum_num = x + y
    avg = sum_num / 2

    return sum_num, avg
a = 5
b = 20
sum3, avg1 = add_x_and_y_return_multi_value(a, b)
print(sum3)
print(avg1)

ls = [5, 9, 6, 4, 56, 478, 78]
def is_odd(x):
    return x % 2 ==1
f_list = list(filter(lambda x: x % 2 ==1, ls))
print(f_list)


