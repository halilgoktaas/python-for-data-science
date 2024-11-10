#alternating fonksiyonunun enumararte ile yazılması
from pyarrow.ipc import new_stream


def alternat(string):
    new_string=""
    for i,letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternat("hi my name is john and i am learning python")