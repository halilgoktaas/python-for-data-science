#enumerate: otomatik counter ile for loop

students = ["john","mark","venessa","mariam"]

for i in students:
    print(i)

for index,student in enumerate(students,1):
    print(index,student)

A = []
B= []

for index,student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)