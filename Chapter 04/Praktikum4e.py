print ("Grafik Mahasiswa PTIK")
mhs_laki = int(input("Masukkan Jumlah Mahasiswa Laki laki : "))
mhs_pr = int(input("Masukkan Jumlah Mahasiswa Perempuan: "))

hasil_laki = int(mhs_laki // 10)
hasil_pr = int(mhs_pr) // 10

print("Laki laki : ", '*' * hasil_laki, ((mhs_laki)))
print("Perempuan : ", '*' * hasil_pr, ((mhs_pr)))
