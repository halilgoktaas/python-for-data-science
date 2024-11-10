#fonksiyonların statement body bölümi
from tornado.gen import multi


#def function_name(parametres)
    #statements(function body)

def say_hi(string):
    print(string)
    print("Merhaba")
    print("Selam")

say_hi("miull")

def multiplic(a,b):
    c= a*b
    print(c)
multiplic(10,9)

#girilen değerleri liste içinde saklayacak fonksiyon
list_store= []

def add_element(a,b):
    c=a*b
    list_store.append(c)
    print(list_store)

add_element(1,8)
add_element(18,8)
add_element(180,10)
