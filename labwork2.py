class Student:
    def __init__(self, id, name, birthday):
        self.__id = id
        self.__name = name
        self.__birthday = birthday

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getBirthday(self):
        return self.__birthday

    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student Name: ")
        self.__birthday = input("Student Birthday: ")

    def __str__(self):
        return "Student: " + self.__name + " has id is " + self.__id + " has birthday on " + self.__birthday

    def description(self):
        print(self.__str__())


class Mark:
    def __init__(self, stname, course, mark=0):
        self.__stname = stname
        self.__course = course
        self.__mark = mark

    def input(self):
        print("Student: {self.STname} mark ")
        self.__mark = input("in {self.course}: ")

    def getMark(self):
        return self.__mark

    def getCourse(self):
        return self.__course

    def getName(self):
        return self.__stname

    def __str__(self):
        return "Student " + self.__stname.TakeName() + " : Mark of " + str(
            self.__mark) + " in course of " + self.__course

    def description(self):
        print(self.__str__())


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def input(self):
        self.__id = input("Course Id: ")
        self.__name = input("Course Name: ")

    def __str__(self):
        return "Course: " + self.__name + " has id:  " + self.__id

    def description(self):
        print(self.__str__())


Listst = []
ListCourse = []
Marks = []

totalstd = int(input("Enter number of Students: "))

for i in range(totalstd):
    st = Student()
    st.input()
    Listst += [st]

for student in Listst:
    print(student)

totalcourse = int(input("Enter number of Courses: "))

for i in range(totalcourse):
    course = Course()
    course.input()
    totalcourse += [course]

for c in ListCourse:
    print(c)


def Choosecourse():
    Course = input("Enter the course name: ")
    return Course


def inputMark(Course):
    for i in range(totalcourse):
        if Course == ListCourse[i].getName():
            for j in range(totalstd):
                m = Mark(Listst[j].getName(), ListCourse[i].getName())
                m.input()
                Marks.append(m)


def outputMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark()])


inputMark(Choosecourse())
inputMark(Choosecourse())
outputMark(Choosecourse())
outputMark(Choosecourse())