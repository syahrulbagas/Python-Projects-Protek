import math
print("Liter bensin yang diperlukan ? ")

jarakTempuh = int(input("Masukkan Jarak Tempuh = "))
literBensin = int(12)

liter = jarakTempuh / literBensin

#bawaan bensin 50 Liter

banyakisi = (liter-50) / 50
print(" Banyak Isi Bensin = " ,math.ceil(banyakisi), "liter")
