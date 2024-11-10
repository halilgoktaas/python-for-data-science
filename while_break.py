#break continue while

salaries = [1000,2000,3000,4000,5000]

for i in salaries:
    if i ==3000:
        break
    print(i)

for i in salaries:
    if i == 3000:
        continue
    print(i)

number = 1
while number < 5:
    print(number)
    number +=1