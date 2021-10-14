class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.a_grade = 0
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def assess_kn(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calc_grade(self.grades)}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return res
    def calc_grade(self,grades):  #Средняя оценка за все курсы
        count = 0
        a_grade = 0
        for grade in grades.values():
            count +=1
            a_grade += mean(grade)
            self.a_grade = a_grade / count
        return self.a_grade
    def __gt__(self, other):
        if isinstance(other, Student):
            return self.a_grade > other.a_grade
        return NotImplemented
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname, a_grade = 0):
        super().__init__(name, surname)
        self.a_grade = a_grade
        self.grades = {}
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calc_grade(self.grades)}'
        return res
    def calc_grade(self, grades):  #Средняя оценка за все курсы
        count = 0
        a_grade = 0
        for grade in grades.values():
            count +=1
            a_grade += mean(grade)
            self.a_grade = a_grade / count
        return self.a_grade
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.a_grade > other.a_grade
        return NotImplemented

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
 
from statistics import mean  


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Mathematics']
some_student = Student('Oruy', 'Mean', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Mathematics']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
some_lecturer = Lecturer('Some', 'Lect')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

cool_reviewer = Reviewer('Mose', 'Dubby')
some_reviewer = Reviewer('Moste', 'Dubbly')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(some_student, 'Python', 9)
cool_reviewer.rate_hw(some_student, 'Python', 9)
cool_reviewer.rate_hw(some_student, 'Python', 7)

best_student.assess_kn(cool_lecturer, 'Python', 9)
best_student.assess_kn(cool_lecturer, 'Python', 7)
best_student.assess_kn(cool_lecturer, 'Python', 6)
best_student.assess_kn(some_lecturer, 'Python', 9)
best_student.assess_kn(some_lecturer, 'Python', 8)
best_student.assess_kn(some_lecturer, 'Python', 8)

print(best_student)
print(some_student)
print(cool_lecturer)
print(some_lecturer)
print(cool_reviewer)
print(some_reviewer)


print(some_student > best_student)
print(some_lecturer > cool_lecturer)

students = [
    {'Surname':some_student.surname, 'course':'Python', 'grade':some_student.a_grade},
    {'Surname':best_student.surname,'course':'Python', 'grade':best_student.a_grade},
    {'Surname':some_student.surname, 'course':'Git', 'grade':some_student.a_grade},
    {'Surname':best_student.surname, 'course':'Git', 'grade':best_student.a_grade},
]


def calc_grade_s(students, course_name):  #Средняя оценка за указанный курс для студентов
    grade = 0
    c = 0
    for student in students:
      if course_name == student['course']:
                grade += student['grade']
                c += 1
    grade_course = grade / c
    return grade_course
print(calc_grade_s(students, 'Python'))

lecturers = [
    {'Surname':some_lecturer.surname, 'course':'Python', 'grade':some_lecturer.a_grade},
    {'Surname':cool_lecturer.surname,'course':'Python', 'grade':cool_lecturer.a_grade},
    {'Surname':some_lecturer.surname, 'course':'Git', 'grade':some_lecturer.a_grade},
    {'Surname':cool_lecturer.surname, 'course':'Git', 'grade':cool_lecturer.a_grade},
]
def calc_grade_l(lecturers, course_name):  #Средняя оценка за указанный курс для лекторов
    grade = 0
    c = 0
    for lecturer in lecturers:
      if course_name == lecturer['course']:
                grade += lecturer['grade']
                c += 1
    grade_course = grade / c
    return grade_course
print(calc_grade_l(lecturers, 'Python'))