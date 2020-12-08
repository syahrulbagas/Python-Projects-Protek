while True:
    try:
        InputNama = int(input("Ingin memasukkan berapa nama?: "))
        break
    except:
        print("Masukkan hanya angka")
        continue
    else:
        exit()
print("Nama akan diinputkan".format(InputNama))

ListNama= []
while (InputNama > 0):
    TambahData = str(input("Masukkan nama: "))
    ListNama = ListNama + [TambahData]
    InputNama -= 1
ListNama.sort()
print("\nList Nama:")
for i in ListNama:
    print("{0} ({1} karakter)".format(i,len(i)))
