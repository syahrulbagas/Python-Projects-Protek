buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
while True:
    namabuah = input('Silahkan Masukan nama buah  : ')
    if namabuah in buah:
        try:
            kilo = int(input('Berapa Kg... : '))
            harga = kilo * buah[namabuah]
            print('Total harga = Rp', harga)
        except (ValueError):
            break
    elif (namabuah == '') or (namabuah not in buah):
        print('Maaf nama buah yang anda masukkan salah')
