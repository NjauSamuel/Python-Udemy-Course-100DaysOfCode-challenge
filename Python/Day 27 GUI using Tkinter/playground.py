# Python has an inbuilt unlimited number of arguments for functions which is args and initialized by an asterix

# For Example:
#     if I want to add an unlimited number of numbers using a functions the following is the function.

# def add(*args):
#     numbers = 0
#     for n in args:
#         numbers += n
#     return numbers
#
#
# multiples = add(12, 3, 4)
# print(multiples)
# multiples2 = add(23, 12, 56, 78, 34, 56, 78, 1000)
# print(multiples2)
#
#
# def calculate(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
#
# calculate(add=3, multiply=5)
#
#
# def test(*args):
#     print(args)
#
#
# test(1, 2, 3, 4)
#
#
# def all_aboard (a, *args, **kwargs):
#     print(a, args, kwargs)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)

