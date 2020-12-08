def hargaPalingMahal(x):
    harga = list(x.values())
    harga.sort(reverse=True)
    hargaMahal = harga[0]
    for buah, harga in x.items():
        if harga == hargaMahal:
            return buah
buah = {'apel' : 5000, 'jeruk' : 8500 , 'mangga' :  7800, 'duku' : 6500}
print(hargaPalingMahal(buah))
