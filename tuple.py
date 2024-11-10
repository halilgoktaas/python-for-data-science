#denetler tuple
#değiştirilemez
#sıralıdır
#kapsayıcıdır

t = ("john","mark",1,2)
type(t)
t[0]
t[0:3]
#verileri değiştirmek için
t = list(t)
t[0]= 99
t= tuple(t)

