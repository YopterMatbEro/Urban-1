grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# сортируем и преобразовываем множество students в список
students_list = sorted(list(students))

# распределяем оценки студентам и считаем средний балл
students_average_grades = {student: sum(grades[index])/len(grades[index]) for index, student in enumerate(students_list)}

print(students_average_grades)

# простите, что через цикл, но нам же нужно универсальный код делать, а вручную
# прописывать каждый элемент отдельно - фи...
