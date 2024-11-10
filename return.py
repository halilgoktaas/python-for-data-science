#return fonksiyon çıktılarını girdi olarak kullanmak

def calculate(varm,moisture,charge):
    print((varm+moisture)/charge)

calculate(98,12,78) * 10

def calculate(varm,moisture,charge):
    return (varm+moisture)/charge


calculate(98,12,78) * 10