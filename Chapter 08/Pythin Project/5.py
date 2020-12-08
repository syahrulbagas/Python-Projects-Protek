bil = [2,4,5,6]
def kuadrat(bil):
    hasil = []
    for i in bil:
        hasil = hasil + [i**2]
    return hasil
hasil = kuadrat(bil)
print (hasil)
