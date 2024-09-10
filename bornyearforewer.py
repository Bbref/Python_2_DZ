born_year = 0
while born_year != 1799:
    born_year = input("Введите год рождения А.С.Пушкина: ")
    if int(born_year) != 1799:
        print("Неверный год рождения")
    else:
        print("Верно")
        break