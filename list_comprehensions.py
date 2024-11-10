#comprehensions

#list comprehensions
def new_salary(x):
    return x * 20 / 100 + x
salaries = [1000,2000,3000,4000]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries ]

[salary * 2 for salary in salaries ]

[salary * 2 for salary in salaries if salary < 3000]
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

students = ["John","Mark","Venessa","Mariam"]

students_no = ["John","Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]
