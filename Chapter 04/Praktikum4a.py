print ("Tarif Rental Mobil")
print("--------------------------")
print("Biaya Rental /12 jam = Rp.200.000")
print("Biaya rental Tambahan / jam = Rp.10.000")

rentalPertama = 200000
rentaltambahan = 10000

jamPertama = float(06.00)
jamKedua = int(23.50)
hasilJam = round(jamKedua - jamPertama)

waktuRental = int(12)
waktuTambah = hasilJam - waktuRental

biayaTambahan = waktuTambah * 10000
total = rentalPertama + biayaTambahan
print("--------------------------")
print("Biaya Rental Pertama Rp", rentalPertama)
print("Biaya Rental Tambahan Rp", biayaTambahan)
print("Total Biaya Rental Rp", total)
