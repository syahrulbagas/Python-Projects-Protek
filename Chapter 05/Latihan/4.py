# Program Hitung Gaji Karyawan
kodeKaryawan = int(input("Masukkan Kode Karyawan : "))
namaKaryawan = str(input("Masukkan Nama Karyawan : "))
golonganKaryawan = str(input("Masukkan Golongan : "))
if(golonganKaryawan == "A"):
 gajiPokok = 10000000
 potongan = 2.5
elif(golonganKaryawan == "B"):
 gajiPokok = 8500000
 potongan = 2.0
elif(golonganKaryawan == "C"):
 gajiPokok = 7000000
 potongan = 1.5
elif(golonganKaryawan == "D"):
 gajiPokok = 5500000
 potongan = 1.0
else:
 print("Golongan tidak ditemukan")
 exit()
# Hitung Potongan
hitungPotongan = gajiPokok * (potongan/100)
# Tampilan Hasil
print("====================================\n STRUK RINCIAN GAJI KARYAWAN\n-----------------------------------------------------------")
print("Nama Karyawan : {0} (Kode: {1})".format(namaKaryawan,kodeKaryawan))
print("Golongan : {0}".format(golonganKaryawan))
print("-----------------------------------------------------------")
print("Gaji Pokok : Rp {0}".format(gajiPokok))
print("Potongan ({0} %) : Rp {1}".format(potongan,hitungPotongan))
print("----------------------------------------------------------- -")
print("Gaji Bersih : Rp {0}".format(gajiPokok - hitungPotongan))
