born_year = input("Введите год рождения А.С.Пушкина: ")
if int(born_year) == 1799:
    born_day = input("Введите день рождения А.С.Пушкина: ")
    if int(born_day) == 6:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")