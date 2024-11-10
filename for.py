#döngüler loops

#for

students = ["john","mark","venessa","mariam"]

for i in students:
    print(i)

for i in students:
    print(i.upper())

salaries = [1000,2000,3000,4000,5000]

for i in salaries:
    print(i*20/100 + i)

def new_salary(salary,rate):
    return int(salary*rate/100 + salary)

new_salary(1500,10)

for i in salaries:
    print(new_salary(i,10))

for i in salaries:
    if i >= 3000:
        print(new_salary(i, 10))
