import random
users = input("Введите <камень>, <ножницы> или <бумага>")
comp = random.randint(1, 3)
if users == "камень":
    users == 1
elif users == "ножницы":
    users == 2
elif users == "бумага":
    users == 3
else:
    print("Неверный ввод")

if (comp == 1 and users == 1) or (comp == 2 and users == 2) or (comp == 3 and users == 3):
    print(comp, 'vs', users)
    print('Ничья')
elif (comp == 1 and users == 2) or (comp == 2 and users == 3) or (comp == 3 and users == 1):
    print(comp, 'vs', users)
    print('Вы проиграли :(')
else:
    print(comp, 'vs', users)
    print('Вы выиграли!')
