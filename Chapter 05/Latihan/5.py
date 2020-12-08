# Program Hitung Gaji Karyawan
kodeKaryawan = int(input("Masukkan Kode Karyawan : "))
namaKaryawan = str(input("Masukkan Nama Karyawan : "))
golonganKaryawan = str(input("Masukkan Golongan : "))
inputsudahMenikah = int(input("Masukkan status (1:menikah, 2:blm): "))
sudahMenikah = False
if(inputsudahMenikah ==1):
 sudahMenikah = True
 statusMenikah = "Sudah menikah"
else:
 statusMenikah = "Belum menikah"
if(sudahMenikah):
 jumlahAnak = int(input("Masukkan jumlah anak : "))
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
# Hitung Tunjagan
if(sudahMenikah):
 tunjanganIstri = gajiPokok * 10/100
 tunjanganAnak = (gajiPokok * (5/100)) * jumlahAnak
#HITUNG GAJI KOTOR
if(sudahMenikah):
 gajiKotor = gajiPokok + tunjanganIstri + tunjanganAnak
else:
 gajiKotor = gajiPokok
hitungPotongan = gajiPokok * (potongan/100)
# Tampilan Hasil
print("====================================\n STRUK RINCIAN GAJI KARYAWAN\n-----------------------------------------------------------")
print("Nama Karyawan : {0} (Kode: {1})".format(namaKaryawan,kodeKaryawan))
print("Golongan : {0}".format(golonganKaryawan))
print("Status menikah : {0}".format(statusMenikah))
if(sudahMenikah):
 print("Jumlah anak : {0}".format(jumlahAnak))
print("-----------------------------------------------------------")
print("Gaji Pokok : Rp {0}".format(gajiPokok))
if(sudahMenikah):
 print("Tunjangan istri : Rp {0}".format(tunjanganIstri))
 print("Tunjangan anak : {0}".format(tunjanganAnak))
print("----------------------------------------------------------- +")
print("Gaji kotor : Rp {0}".format(gajiKotor))
print("Potongan ({0} %) : Rp {1}".format(potongan,hitungPotongan))
print("----------------------------------------------------------- -")
print("Gaji Bersih : Rp {0}".format(gajiKotor - hitungPotongan))
