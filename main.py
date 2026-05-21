import crud

while True:
    print("1. Створити студента")
    print("2. Створити курс")
    print("3. Отримати всіх студентів")
    print("4. Отримати всі курси")
    print("5. Записати студента на курс")
    print("6. Отримати всіх студентів, які записані на певний курс")
    print("7. Вийти")
    
    choice = input("Виберіть дію: ")
    if choice == '1':
        name = input("Введіть ім'я студента: ")
        age = int(input("Введіть вік студента: "))
        major = input("Введіть спеціальність студента: ")
        crud.create_student(name, age, major)
        print("Студента успішно створено!")
    elif choice == '2':
        course_name = input("Введіть назву курсу: ")
        instructor = input("Введіть ім'я викладача: ")
        crud.create_course(course_name, instructor)
        print("Курс успішно створено!")
    elif choice == '3':
        students = crud.get_students()
        print("Список студентів:")
        for student in students:
            print(f"{student[0]}. {student[1]} - {student[2]} - {student[3]}")
    elif choice == '4':
        courses = crud.get_courses()
        print("Список курсів:")
        for course in courses:
            print(f"{course[0]}. {course[1]} - {course[2]}")