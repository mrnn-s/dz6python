# Было

#3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

#my_list=["qwe", "asd", "zxc", "qwe", "ertqwe"]

#print(my_list)

#search=input('enter search number:')
#count=0
#position=0
#for item in my_list:
    #if search == item:
#         count+=1
#     if count ==2:
#         break
#     position+=1
# if count >=2:
#     print(position)
# else:
#     print("-1")
#стало 

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(my_list)
search = input("Enter search string: ")
count = 0
position = -1
for i, item in enumerate(my_list):
    if search == item:
        count += 1
        if count == 2:
            position = i
            break

print(position)