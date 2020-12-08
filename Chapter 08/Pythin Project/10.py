daftarbuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print (daftarbuah,'\n')
total = []
while True :
    try:
        namabuah = input ("Silakan masukkan nama buah yang ingin anda beli : ")
        if namabuah in daftarbuah:
            kilo = int ( input ("Berapa (Kg)             : "))
            hargaakhir = kilo * daftarbuah[namabuah]
            total.append(hargaakhir)
            konfirmasi = input ("Apakah anda ingin membeli buah yang lain? (y/n) : ")
            if (konfirmasi != 'y'):
                break
        elif (namabuah == '') or (namabuah not in daftarbuah):
            print ("Maaf, buah yang ingin Anda beli tidak ada di dalam daftar")
    except (ValueError):
            print ("Silakan masukkan jumlah (Kg) yang benar")
print("Total harga                 : Rp", sum(total)) 
