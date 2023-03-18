import random


def select_best_students(filename):
    # Считывание данных из файла
    with open(filename, "r") as file:
        students = [line.strip().split(", ") for line in file.readlines()]

    # Отбор лучших студентов
    best_students = {}
    for fio, gender, course, gpa in students:
        if course not in best_students.keys():
            best_students[course] = {"M": [], "F": []}
        best_students[course][gender].append((fio, float(gpa)))
        if gender == "M":  # Ищем лучших студентов из парней
            if best_students[course]["M"] is None or len(best_students[course]["M"]) == 0 or float(gpa) > \
                    best_students[course]["M"][0][1]:
                best_students[course]["M"] = [(fio, float(gpa))]
            elif float(gpa) == best_students[course]["M"][0][1]:
                best_students[course]["M"].append((fio, float(gpa)))
        elif gender == "F":  # Ищем лучших студентов из девушек
            if best_students[course]["F"] is None or len(best_students[course]["F"]) == 0 or float(gpa) > \
                    best_students[course]["F"][0][1]:
                best_students[course]["F"] = [(fio, float(gpa))]
            elif float(gpa) == best_students[course]["F"][0][1]:
                best_students[course]["F"].append((fio, float(gpa)))
    selected_students = []
    for course in best_students.keys():  # Составляем пары (если студент без пары, то никто не идет)
        male_students = best_students[course]["M"]
        female_students = best_students[course]["F"]
        if male_students and female_students:
            selected_students.append(random.choice(male_students) + (course,))
            selected_students.append(random.choice(female_students) + (course,))
    return selected_students


def test_cases():
    with open("tests.txt", "w") as tests:
        # Тест 1: на курсе студенты одного пола
        if not select_best_students("input01.txt"):
            tests.write("Test 1: passed\n")
        else:
            tests.write("Test 1: failed.\n")
            tests.write(", ".join(map(str, select_best_students("input01.txt"))) + "\n")

        # Тест 2: на курсе есть одинаковые оценки у студентов
        if len(select_best_students("input02.txt")) == 2:
            tests.write("Test 2: passed\n")
            tests.write(", ".join(map(str, select_best_students("input02.txt"))) + "\n")
        else:
            tests.write("Test 2: failed.\n")
            tests.write(", ".join(map(str, select_best_students("input02.txt"))) + "\n")

        # Тест 3: на курсе только один студент
        if not select_best_students("input03.txt"):
            tests.write("Test 3: passed\n")
        else:
            tests.write("Test 3: failed.\n")
            tests.write(", ".join(map(str, select_best_students("input03.txt"))) + "\n")

        # Тест 4: обычный случай
        if len(select_best_students("input04.txt")) == 6:
            tests.write("Test 4: passed\n")
            tests.write(", ".join(map(str, select_best_students("input04.txt"))) + "\n")
        else:
            tests.write("Test 4: failed.\n")
            tests.write(", ".join(map(str, select_best_students("input04.txt"))) + "\n")

        # Тест 5: все студенты на курсе имеют разную успеваемость
        if len(select_best_students("input05.txt")) == 2:
            tests.write("Test 5: passed\n")
            tests.write(", ".join(map(str, select_best_students("input05.txt"))) + "\n")
        else:
            tests.write("Test 5: failed.\n")
            tests.write(", ".join(map(str, select_best_students("input05.txt"))) + "\n")


# Проводим тесты
test_cases()

# Вывод результата
n = 0  # счетчик
with open("output.txt", "w") as outFile:
    outFile.write("Список студентов, отправляющихся на новогодний бал.\n")
    for fio, gpa, course in select_best_students("input.txt"):
        if n % 2 == 0:
            outFile.write("От " + str(course) + " курса:\n")
            outFile.write(fio + " (" + str(gpa) + ")\n")
            n += 1
        else:
            outFile.write(fio + " (" + str(gpa) + ")\n")
            n += 1
