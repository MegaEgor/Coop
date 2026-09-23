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
    print("неверный ввод")

