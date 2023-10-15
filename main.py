#задача 1
#
# x = int(input())
# a = 0
# for i in range(2, x // 2 + 1):
#     if x % i == 0:
#         a = a + 1
# if a <= 0:
#     print('Число', x, 'простое')
# else:
#     print('Число', x, 'не простое')





#задача 2
#
# x = [3, -9, 6, 7, 0, 2]
# a = len(x)
# for i in range(1, a):
#     for j in range(a - 1, i - 1, -1):
#         if x[j - 1] > x[j]:
#             x[j - 1], x[j] = x[j], x[j - 1]
# print(*x)





# задача 3
#
# from random import randrange
# x = [randrange(-10,11) for i in range(10)]
#
# print(x)
# print(max(x))





# задача 4
#
# x = int(input())
# a = 0
# b = 1
#
# for i in range (1, x):
#     c = a + b
#     a = b
#     b = c
# print(b)




# задача 5
#
# from random import randrange
# x = [randrange(-10,11)for i in range(10)]
# a = {x.count(i): i for i in set(x)}
# print(x)
# print(a[max(a)])