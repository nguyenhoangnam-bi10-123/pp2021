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
