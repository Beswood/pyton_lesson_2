'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# a = 5
# for i in range(a):
#     i+=1
#     for j in range(1):
#        print(str(i)," ", str(j))

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# a = int(input())
# Не понял условие задачи


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# sum = 1
# for i in range(1,10):
#    sum*=i
#
# print(sum)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 234565679654
# i = 0
# while integer_number > 0:
#     r =integer_number % 10
#     i+=r
#     integer_number = integer_number//10
#
# print(i)


'''
Задача 7
Найти произведение цифр числа.
'''

# integer_number = 34567
# i = 1
# while integer_number > 0:
#     r =integer_number % 10
#     i *= r
#     integer_number = integer_number//10
# print(i)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''

integer_number = 123095678
a = 0
while integer_number > 0:
    b = integer_number%10
    if a < b:
        a = b
    integer_number = integer_number//10
print(a)


'''
Задача 10
Найти количество цифр 5 в числе
'''
# integer_number = 15151111111
# i = 0
# while integer_number>0:
#     if integer_number%10 == 5:
#         i+=1
#     integer_number = integer_number//10
# print(i)