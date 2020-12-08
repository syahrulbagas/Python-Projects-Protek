#membuka dan membaca file d:/data.txt
try :
    file = open("d:/data.txt", "r")

#baca baris pertama file
#simpan ke dalam variabel bil1 sbg integer
    bil1 = int(file.readline())

#baca baris pertama file
#simpan ke dalam variabel bil2 sbg integer
    bil2 = int(file.readline())

#hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, 'samadengan', hasil)
except FileNotFoundError:
    print('File tidak ditemukan')
except ZeroDivisionError:
    print('Tidak boleh dibagi sama dengan 0')
