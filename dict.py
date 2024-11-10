#sözlük dict
#değiştirilebilir
#sırasız
#kapsayıcı
#key-value

sozluk= {"REG": "Regression",
         "Log": "Logistic",
         "Cart" : "Class"

         }
sozluk["REG"]

#key sorgulama
"REG" in sozluk
sozluk.get("REG")

#value değiştirmek
sozluk["REG"] = ["YSA",10]

#tüm keylere erişmek
sozluk.keys()
sozluk.values()
sozluk.items()

#key value değerini güncellemek
sozluk.update({"RF": 10})
