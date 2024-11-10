#kümeler set
#değiştirilebilir
#sırasız + eşsizdir
#kapsayıcıdır

#difference iki kümenin farkı
set1= set([1,3,5])
set2= set([1,2,3])
#set1 de olup set 2 de olmayanlar
set1.difference(set2)
#tersi
set2.difference(set1)

#synmetric_diffrence iki kümede de birbirlerine göre olmayanlar
set1.symmetric_difference(set2)

#iki kümenin kesişimi instersection

set1.intersection(set2)
set2.intersection(set1)
set1 & set2

#iki kümennin birleşimi union
set1.union(set2)
set2.union(set1)

#iki kümenin kesişimi boş mu? isdisjoint
set1.isdisjoint(set2)

#bir küme diğer kümenin alt kümesi mi issubset
set1.issubset(set2)

#bir küme diğer kümeyi kapsıyor mu
set2.issuperset(set1)