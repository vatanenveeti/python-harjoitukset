def parilliset(lista):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

testi_lista = [1,2,3,4,5,6,7,8,9,10,101,102]
print(parilliset(testi_lista))