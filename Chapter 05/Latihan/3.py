# Input Nilai
nilaiBahasaIndonesia = int(input("Masukkan nilai bahasa Indonesia : "))
nilaiIpa = int(input("Masukkan nilai IPA : "))
nilaiMatematika = int(input("Masukkan nilai Matematika : "))
# Mulai Perhitungan
lulusBahasaIndonesia = False
lulusMatematika = False
lulusIpa = False
if(nilaiBahasaIndonesia>60):
 lulusBahasaIndonesia = True
if(nilaiIpa>60):
 lulusIpa = True
if(nilaiMatematika>70):
 lulusMatematika = True
# Perhitungan
rangeNilai = range(0,101)
if((nilaiBahasaIndonesia or nilaiIpa or nilaiMatematika) in rangeNilai):
 if(lulusBahasaIndonesia and lulusIpa and lulusMatematika):
    statusKelulusan = "LULUS"
 else:
    statusKelulusan = "TIDAK LULUS"
 print("Status Kelulusan: {0}".format(statusKelulusan))
 print("Sebab:")
 if(not lulusBahasaIndonesia):
    print("- Nilai Bahasa Indonesia kurang dari 60")
 if(not lulusIpa):
    print("- Nilai IPA kurang dari 60")
 if(not lulusMatematika):
    print("- Nilai Matematika kurang dari 70")
else:
 print ("Maaf Nilai yang Anda Masukkan Tidak Valid")
