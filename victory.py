people = [
    ("Владимир Ленин", 1870),
    ("Александр Пушкин", 1799),
    ("Юрий Гагарин", 1934),
    ("Дмитрий Менделеев", 1834),
    ("Михаил Ломоносов", 1711)
]

total_questions = len(people)
right_answers = 0
wrong_answers = 0

while True:
    right_answers = 0
    wrong_answers = 0
    for i in range(total_questions):
        current_person = people[i]
        question = f"Какой год рождения у {current_person[0]}?"
        answer = input(question + ": ")
        if int(answer) == current_person[1]:
            right_answers += 1
        else:
            wrong_answers += 1

    print(f"Количество правильных ответов: {right_answers}")
    print(f"Количество неправильных ответов: {wrong_answers}")
    print(f"Процент правильных ответов: {round((right_answers / total_questions) * 100, 2)}%")
    print(f"Процент неправильных ответов: {round((wrong_answers / total_questions) * 100, 2)}%")

    play_again = input("Хотите сыграть снова? (да/нет): ")
    if play_again not in ["да", "yes"]:
        break

print("Благодарим за участие! До новых встреч!")