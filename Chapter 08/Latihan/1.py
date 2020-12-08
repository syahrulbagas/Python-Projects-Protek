import math

a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)

print("\nSisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b") 
a.insert(3, 10)
b.insert(2,15)
print(a)
print(b)

print("\nSisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b")
a.append(4)
b.append(8)
print(a)
print(b)

print("\nKemudian lakukan sorting secara ascending pada list a dan b")
a.sort()
b.sort()
print(a)
print(b)

print("\nBuatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)")
c = a[0:8]
d = b[2:10]
print(c)
print(d)

print("\nBuatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya.")
e = []
i = 0
for i in range(len(c)):
    x =  c[i] + d[i]
    e = e +[x]
print(e)

print("\nUbahlah list e ke dalam tuple")
theTuple = tuple(e)
print(theTuple)

print("\nCarilah nilai min, maks, dan jumlahan seluruh elemen dari e")
nilaiMin = min(theTuple)
nilaiMax = max(theTuple)
totalTup = sum(theTuple)
print(nilaiMin)
print(nilaiMax)
print(totalTup)

print("\nBuatlah sebuah string myString = “python adalah bahasa pemrograman yang menyenangkan”")
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)

print("\nDengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut")
hurufPenyusun = set(myString)
print(hurufPenyusun)

print("\nUrutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list.")
theList = list(hurufPenyusun)
theList.sort()
print(theList)
