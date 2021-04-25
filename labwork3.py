from math import *

class Student:
    def __init__(self, id="", name="", birthday=""):
        self.id = id
        self.name = name
        self.birthday = birthday

    def TakeId(self):
        return self.id

    def TakeName(self):
        return self.name

    def TakeBirthday(self):
        return self.birthday

    def input(self):
        self.id = input("Student Id: ")
        self.name = input("Student Name: ")
        self.birthday= input("Student Birthday: ")

    def __str__(self):
        return "Student: " + self.name + " has id " + self.id + " has birthday on " + self.birthday

    def description(self):
        print(self.__str__())


class Mark:
    def __init__(self, stname, course, mark=0, credit=0 ,GPA=0):
        self.stname = stname
        self.course = course
        self.credit = credit
        self.mark = mark
        self.GPA = GPA

    def input(self):
        print("Student mark: {self.stname}")
        self.mark = float(input("of course {self.course}: "))
        self.credit = Course.getCredit(course)

    def TakeMark(self):
        return floor(self.mark * 10) / 10

    def TakeCourse(self):
        return self.course

    def TakeGPA(self):
        return floor(self.GPA * 10) / 10

    def TakeGPA(self, GPA):
        self.GPA = GPA

    def TakeName(self):
        return self.stname

    def TakeCredit(self):
        return self.credit

    def __str__(self):
        return "Name Student: "  + self.stname.getName() + " , mark: " + str(
            self.TakeMark()) + " of course " + str(self.course)

    def description(self):
        print(self.__str__())


class Course:
    def __init__(self, id="", name="", credit=0):
        self.id = id
        self.name = name
        self.credit = credit

    def TakeId(self):
        return self.id

    def getName(self):
        return self.name

    def TakeCredit(self):
        return self.credit

    def input(self):
        self.id = input("Course Id: ")
        self.name = input("Course Name: ")
        self.credit = int(input("credit : "))

    def __str__(self):
        return "Course: " + self.name + " has id " + self.id + " and credit of " + str(self.credit)

    def description(self):
        print(self.__str__())


Totalst = []
Listcourse = []
Marks = []

# find the number of students
NumberStd = int(input("Enter number of Students: "))


for i in range(NumberStd):
    s = Student()
    s.input()
    Totalst += [s]

for student in Totalst:
    print(student)


NumberOfCourse = int(input("Enter number of Courses: "))


for i in range(NumberOfCourse):
    c = Course()
    c.input()
    Listcourse += [c]


for c in Listcourse:
    print(c)


# choose a course
def choseCourse():
    Course = input("Enter the course name: ")
    return Course


# input marks for all student in a Course
def inputMark(Course):
    for i in range(NumberOfCourse):
        if Course == Listcourse[i].getName():
            for j in range(NumberStd):
                m = Mark(Totalst[j].getName(), Listcourse[i].getName(), Listcourse[i].getCredit())
                m.input()
                Marks.append(m)



def outputMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark(), mark.getCredit()])


def TakeStudent():
    stdName = input(" a Student name: ")
    return stdName


def averageMark(Name):
    x = y = 0
    for mark in Marks:
        if mark.getName() == Name:
            x += mark.getMark() * mark.getCredit()
            y += mark.getCredit()

    AverageMark = x / y
    AverageMark_fld = floor(AverageMark * 10) / 10
    print("Average Mark for " + Name + ": " + str(AverageMark_fld))

    for mark in Marks:
        if mark.getName() == Name:
            mark.setGPA(AverageMark_fld)


for course in Listcourse:
    print("MARKS:")
    inputMark(choseCourse())
for std in Totalst:
    print("GPA:")
    averageMark(TakeStudent())
