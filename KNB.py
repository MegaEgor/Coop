import random
again = 1

while again == 1:
    
    users = input("Введите <камень>, <ножницы> или <бумага>: ")
    user = users
    comp = random.randint(1, 3)

    if users == "камень":
        users = 1
    elif users == "ножницы":
        users = 2
    elif users == "бумага":
        users = 3
    else:
        print("Неверный ввод")
        continue

    if (comp == 1 and users == 1) or (comp == 2 and users == 2) or (comp == 3 and users == 3):
        result = 'Ничья'
    elif (comp == 1 and users == 2) or (comp == 2 and users == 3) or (comp == 3 and users == 1):
        result = 'Вы проиграли :('
    else:
        result = 'Вы выиграли!'
    
    if comp == 1:
        comp = "камень"
    elif comp == 2:
        comp = "ножницы"
    else:
        comp = "бумага"
    
    print('Компьютер:', comp, 'vs', 'Ваш выбор:', user)
    print(result)

    again = int(input('Хотите сыграть еще раз? Если да, введите 1, если нет, введите 0: '))
