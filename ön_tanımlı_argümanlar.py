#ön tanımlı argümanlar

def divide(a,b):
    print(a/b)

divide(1,2)

def divide(a, b=1):
    print(a/b)

divide(1)
divide(10)