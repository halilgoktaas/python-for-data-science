#else

def number_check(number):
    if number ==10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)
number_check(10)

#elif
def number_check(number):
    if number > 10:
        print("10 dan büyük")
    elif number < 10:
        print("10 dan küçük")
    else:
        print("10 a eşit")
number_check(12)
number_check(10)
number_check(9)