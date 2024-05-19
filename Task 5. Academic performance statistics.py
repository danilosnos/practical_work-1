subjects = []


# Ввод предметов
def read_subjects():
    while True:
        subject = input("Введите предмет: ")
        if subject == "стоп":
            break
        subjects.append(subject)


read_subjects()

students = []


# Ввод студентов
def read_students():
    while True:
        student = input("Введите фамилию и имя студента через пробел: ")
        if student == "стоп":
            break
        students.append(student.split())


read_students()


# Ввод оценок студентов
def read_scores():
    scores = []
    for student in students:
        scores.append({})
        print("Оценки для студента", student[0], student[1])
        for subject in subjects:
            score = int(input(subject + ": "))
            scores[-1][subject] = score
    return scores


student_scores = read_scores()


# Статистика успеваемости
def statistics():
    max_avg_score = 0
    best_student = ""
    avg_scores = {subject: 0 for subject in subjects}
    count = {subject: 0 for subject in subjects}

    for i, student in enumerate(students):
        total_score = 0
        for subject in subjects:
            total_score += student_scores[i][subject]
            avg_scores[subject] += student_scores[i][subject]
            count[subject] += 1

        avg_score = total_score / len(subjects)
        if avg_score > max_avg_score:
            max_avg_score = avg_score
            best_student = " ".join(student)

    print("\nСтатистика:")
    print("Студент с лучшей успеваемостью:")
    print(best_student + ":", format(max_avg_score, '.2f'))

    print("\nСредний балл по предмету:")
    for subject in subjects:
        avg_scores[subject] = avg_scores[subject] / count[subject]
        print(subject + ":", format(avg_scores[subject], '.2f'))


statistics()