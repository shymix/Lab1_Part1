class Student:
    def __init__(self, name, surname, grades):
        self.__name = name
        self.__surname = surname
        self.__grades = grades

    def name(self):
        return self.__name

    def surname(self):
        return self.__surname

    def grades(self):
        return self.__grades


class Group:
    def __init__(self, a):
        self.__students = {}
        for i in a:
            t = False
            for y in self.__students:
                if i.name() == y.name() and i.surname() == y.surname:
                    print("There can't be 2 simular students in 1 group")
                    t = True
            if not t:
                self.__students[i] = 0

    def average(self):
        students = []
        average_marks = []
        for student in self.__students:
            suma = 0
            amount = 0
            for mark in student.grades():
                suma = suma + mark
                amount = amount + 1
            self.__students[student] = suma / amount
            students.append(f"{student.name()} {student.surname()}")
            average_marks.append(self.__students[student])
        help_mark = 0
        help_student = 0
        a = len(average_marks)
        while a != 2:
            for i in range(0, a-1):
                if average_marks[i] > average_marks[i + 1]:
                    help_mark = average_marks[i]
                    average_marks[i] = average_marks[i + 1]
                    average_marks[i + 1] = help_mark

                    help_student = students[i]
                    students[i] = students[i + 1]
                    students[i + 1] = help_student
            a = a - 1
        for i in range(1, 6):
            print(students[-i], average_marks[-i])


a = Student("a", "a", [1, 2, 3, 4, 2])
b = Student("b", "b", [2, 3, 4, 5, 3])
c = Student("c", "c", [3, 4, 5, 4, 1])
d = Student("d", "d", [1, 5, 3, 3, 2])
e = Student("e", "e", [5, 1, 3, 4, 3])
f = Student("f", "f", [2, 2, 3, 4, 3])
g = Student("g", "g", [4, 3, 3, 4, 5])
h = Student("h", "h", [3, 4, 3, 4, 4])
i = Student("i", "i", [1, 5, 3, 4, 5])
j = Student("j", "j", [10, 10, 10, 10, 10])

students = []
students.append(a)
students.append(b)
students.append(c)
students.append(d)
students.append(e)
students.append(f)
students.append(g)
students.append(h)
students.append(i)
students.append(j)
group = Group(students)
group.average()
