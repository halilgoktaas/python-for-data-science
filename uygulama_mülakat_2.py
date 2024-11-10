#uygulama-mülakat sorusu
from dask.array.numpy_compat import divide

#divide_students fonksiyonu yazınız
#çift indexte yer alan öğrencileri bir listeye alınız
#tek indexte yer alan öğrencileri başka listeye alınız
#fakat bu iki liste tek bir liste olarak return olsun

students= ["John","Mark","Venessa","Mariam"]

def divide_students(students):
    groups = [[],[]]
    for index,student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

divide_students(students)