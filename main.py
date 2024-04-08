class Student:
    """
    Этот класс позволяет работы со студентами, их оценками и курсами, которые они изучают, 
    а также обеспечивает функционал для сравнения студентов по их успеваемости. """

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.grades = {}
        self.courses_in_progress = []
        self.average = 0
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        grades_value = len(*self.grades.values())
        self.average = sum(*self.grades.values()) / grades_value

        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average < other.average

        else: 
            return 'Можно сравнивать только студентов!'
class Mentor:
    """Инициализатор _init_ для определения атрибутов класса Mentor
        Содержит атрибуты:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        """
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    """Этот класс предоставляет возможность работать с 
        экземплярами студентов и преподавателями, их оценками
        и сравнивать их между собой по успеваемости ведения лекций."""
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = 0

    def __str__(self):
        grades_values = len(*self.grades.values())
        self.average = sum(*self.grades.values()) / grades_values

        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average}'
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average < other.average

        else: 
            print('Можно сравнивать только лекторов!')

class Reviewer(Mentor):
    '''Этот класс обеспечивает функционал для рецензирования домашних заданий студентов
       и добавляет оценки в их список оценок для соответствующих курсов.'''
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Создаем экземпляры класса Student
student1 = Student('Egor', 'Sidorov')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Pavel', 'Ivanov')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование']

# Создаем экземпляры класса Lecturer
lecturer1 = Lecturer('Oleg', 'Petrov')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Igor', 'Chernov')
lecturer2.courses_attached += ['Git']

# Создаем экземпляры класса Reviewer
reviewer1 = Reviewer('Nikolay', 'Vivaldi')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Elena', 'Nikitina')
reviewer2.courses_attached += ['Python', 'Git']


# Выставляем оценки за лекции студентам
student1.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Python', 9)


student1.rate_hw(lecturer2, 'Git', 10)
student1.rate_hw(lecturer2, 'Git', 9)


student2.rate_hw(lecturer1, 'Python', 9)
student2.rate_hw(lecturer1, 'Python', 9)


student2.rate_hw(lecturer2, 'Git', 8)
student2.rate_hw(lecturer2, 'Git', 9)


# Выставляем оценки за домашние задания
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)


reviewer1.rate_hw(student2, 'Git', 10)
reviewer1.rate_hw(student2, 'Git', 10)


reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 7)

reviewer2.rate_hw(student2, 'Git', 9)
reviewer2.rate_hw(student2, 'Git', 7)

print(f'Перечень студентов: {student1}  \n{student2}\n')

print(f'Перечень лекторов: {lecturer1} \n {lecturer2}\n')

print(f'Перечень проверяющих: {reviewer1} \n {reviewer2}\n')

print(f'Результат сравнения студентов по средним оценкам за ДЗ: '
      f'{student1.name} {student1.surname} < {student2.name} {student2.surname} = {student1 > student2}')


print(f'Результат сравнения лекторов по средним оценкам за лекции): '
      f'{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname} = {lecturer1 > lecturer2}\n')


# Создаем списки студентов и лекторов
all_students = [student1, student2]

all_lecturers = [lecturer1, lecturer2]


# Функция для вычисления средней оценки студентов
def average_hw_grade_of_students(students, course):
    summi = 0
    count = 0

    for student in students:
        if course in student.grades:
            summi += sum(student.grades[course])
            count += len(student.grades[course])

    return f'Средняя оценка за домашние задания по курсу {course}: {summi / count}'

print(average_hw_grade_of_students(all_students, 'Python'))
print(average_hw_grade_of_students(all_students, 'Git'))

# Функция для вычисления средней оценки лекторов
def average_hw_grade_of_lecturers(lecturers, course):
    summi = 0
    count = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            summi += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])

    return f'Средняя оценка за лекции по курсу {course}: {summi / count}'

print(average_hw_grade_of_lecturers(all_lecturers, 'Git'))
print(average_hw_grade_of_lecturers(all_lecturers, 'Python'))