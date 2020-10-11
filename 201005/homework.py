class Student:
    def __init__(self):
        self.surname = None
        self.name = None
        self.patronymic = None
        self.birthdate = None
        self.group = None


class Teacher:
    def __init__(self):
        self.surname = None
        self.name = None
        self.patronymic = None
        self.discipline = None


class Group:
    def __init__(self):
        self.specialty = None
        self.number_of_students = None
        self.id_of_students = None
        self.patronymic = None
        self.curator = None
        self.number = None


class College:
    def __init__(self):
        self.principal = None
        self.administration = None
        self.number_of_teachers = None
        self.training_group = None
        self.number_of_students = None


class Examination:
    def __init__(self):
        self.teacher = None
        self.discipline = None
        self.mark = None
        self.data = None
        self.time_for_exam = None
        self.gradebook = None


class Student_on_the_exam:
    def __init__(self):
        self.surname = None
        self.name = None
        self.patronymic = None
        self.teacher = None
        self.discipline = None
        self.presence = None
        self.question_number = None


class Car:
    def __init__(self):
        self.type = None
        self.color = None
        self.mileage = None
        self.year_of_issue = None
        self.brand = None

