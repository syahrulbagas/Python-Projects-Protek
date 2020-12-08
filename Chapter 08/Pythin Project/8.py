buah = {'apel' : 5000, 'jeruk' : 8500 , 'mangga' :  7800, 'duku' : 6500}
def rataRataHarga(x):
    harga = list(x.values())
    jumlah = 0
    bagi = 0
    for i in harga:
        jumlah = jumlah + i
        bagi += 1
    rataRata = jumlah/bagi
    return rataRata
        
print(rataRataHarga(buah))
