string = ""

x = int(input("Masukkan Angka :"))
bar = x
while bar >= 0:
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1	
	kiri = 1
	while kiri < (x - (bar-1)):
		string = string + " * "
		kiri = kiri + 1
	kanan = 1
	while kanan < kiri -1:
		string = string + " * "
		kanan = kanan + 1	

	string = string + "\n"
	bar = bar - 1

print (string)
