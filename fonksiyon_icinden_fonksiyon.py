#fonksiyon içierisinden fonksiyon çağırmak

def calculate (varm,mouisture,charge):
    return int((varm+mouisture)/ charge)

calculate(90,12,12) * 10

def standart(a,p):
    return a*10 / 100*p*p
standart(45,1)

def toplam_hesaplama(varm,mouisture,charge,p):
    a = calculate(varm,mouisture,charge)
    b= standart(a,p)
    print(b*10)

toplam_hesaplama(1,3,5,12)