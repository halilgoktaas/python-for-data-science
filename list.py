#listeler
#değiştirilebilir
#sıralıdır indexleri vardır
#kapsayıcıdır

notes = [1,2,3,4]
type(notes)
names = ["a","b","c","d"]
not_nam = [1,2,3,"a","b",True,[1,2,3]]
not_nam[0]
not_nam[5]
not_nam[6][1]

notes[0] = 99

not_nam[0:4]

#liste metodları
dir(notes)

#len
len(notes)
len(not_nam)

#append listeye ekleme yapar
notes
notes.append(100)

#pop indexe göre elemen siler
notes
notes.pop(0)

#insert indexe belirli elemena göre ekler
notes
notes.insert(2, 99)
