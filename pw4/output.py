

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

