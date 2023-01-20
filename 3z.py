#Бвло
# 2. Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# number=float(input("введите дробное число:"))
# if number==int(number):
#     print('целое число')
# else :
#  print(int(number *10 %10))
 
number = float(input("Enter a decimal number: "))

result = "целое число" if int(number) == number else int(number * 10 % 10)
print(result)