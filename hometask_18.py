"""  Документация:
    5 видов предметов 'OOP, Procedure approach, Dynamic approach, Project management, Final project'
    4 вида стаусов = 'sent - когда учитель отправил студенту,
    waiting approve - когда студент решил и отправил учителю,
    accept - когда учителя устроило решение,
    not accept - когда учителя не устроило решение'

    Программа ведет 2 вида списков:
    - журнал учителя (там сводная информация по всем ДЗ и ученикам)
    - дневник каждого студента (информация по ДЗ конкретного студента)
    """

class Tutor:
    students = []
    def __init__(self):
        self.Tutor = Tutor

    def set_hometask(student, subject, status):   # учитель задает ДЗ студенту
        student.students = Student
        student.subject = subject
        student.status = status
        student.student_list.append([subject, status])
        print(f"{student.name} has a new hometask '{subject}' with status '{status}'!" )
        print()
        return Tutor.students.append([student.name, subject, status])

    def check_hometask(student, subject, decision: bool):    # Учитель проверяет ДЗ, если правильно, то True, иначе False
        for i in Tutor.students:             # вносится изменение в журнал учителя
            for j in range(len(i)):
                if i[0] == student.name and i[1] == subject and i[2] == 'waiting approve' and decision == True:
                    i[2] = 'accept'
                elif i[0] == student.name and i[1] == subject and i[2] == 'waiting approve' and decision == False:
                    i[2] = 'not accept'
        for t in student.student_list:       # вносится изменение в дневник студента
            for k in range(len(t)):
                if t[1] == 'waiting approve' and t[0] == subject and decision == True:
                    t[1] = 'accept'
                    print('Dear', student.name,', goog job!')
                    print()
                elif t[1] == 'waiting approve' and t[0] == subject and decision == False:
                    t[1] = 'not accept'
                    print('Dear', student.name,', please try again!')
                    print()

    def get_journal(self):    # Вывести сводный журнал по всем ученикам
        print("   TUTOR's JOURNAL:  ")
        print("The tutor has next students, hometasks and student's progress:")
        for i in range(len(Tutor.students)):
            print(*Tutor.students[i], sep=', ')
        print('    ---    ')

    def course_information(self):   # Информация о курсе
        print('   /////')
        print('In this course we will study next subjects:')
        print('OOP,', 'Procedure approach,', 'Dynamic approach,', 'Project management,', 'Final project')
        print('When a student got hometask the status of hometask will set like "SENT".')
        print('When a student made his hometask the status changed on "WAITING APPROVE"')
        print("After checking, the tutor make decision: 'ACCEPT' if solution is ok, otherwise 'NOT ACCEPT'")
        print('   /////')
class Student:
    def __init__(self, name):
        self.name = name
        self.student_list = []

    def solve(self, subject):   # решить ДЗ, указать предмет, который Студент решает
        for i in self.student_list:    # вносится изменение в дневник студента
            for j in range(len(i)):
                if i[1] == ('sent' or 'not accept') and i[0] == subject:
                    i[1] = 'waiting approve'
                    print(f"Dear Tutor, could you please check my hometask: {i[0]}. Best regards,", self.name)
                    print(f"{self.name}'s hometask: {i[0]} {i[1]} by tutor.")
                    print()
        for i in Tutor.students:       # вносится изменение в журнал учителя
            for j in range(len(i)):
                if i[0] == self.name and i[1] == subject and i[2] == ('sent' or 'not accept'):
                    i[2] = 'waiting approve'

    def get_info_progress(self):  # запрос дневника Студента
        print(self.name, 'has next hometasks with statuses:')
        for i in self.student_list:
            print(*i, sep=', ')
        print('    --- ')




# course = 'OOP, Procedure approach, Dynamic approach, Project management, Final project'
# statuses = 'sent, waiting approve, accept, not accept'

yar = Student('Yaroslav')
peter = Student('Peter')
Tutor.course_information(Tutor)
Tutor.set_hometask(peter, 'Final project', 'sent')
Tutor.set_hometask(yar, 'OOP', 'sent')
Tutor.set_hometask(yar, 'Project management', 'sent')
yar.solve('OOP')
yar.solve('Project management')
peter.solve('Final project')
yar.get_info_progress()
Tutor.check_hometask(yar,'Project management', True)
Tutor.check_hometask(peter,'Final project', False)
Tutor.get_journal(Tutor)
peter.get_info_progress()
