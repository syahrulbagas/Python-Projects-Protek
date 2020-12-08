print("-----------------------------")
print(" PROGRAM HITUNG RATA-RATA")
print("-----------------------------")

InputData = 0
Perhitungan = 0
selesai = False
while not(selesai):
        try:
            TambahData = int(input("Masukkan bilangan bulat: "))
            InputData = InputData + TambahData
            Perhitungan += 1
            choice = None
            while choice not in("y","n"):
                choice = str(input("Lagi (y/n)?: "))
                if(choice == "y"):
                    selesai = False
                elif(choice == "n"):
                    selesai = True
                else:
                    print("Mohon masukkan pilihan (y/n)")
        except ValueError:
            print("Bukan bilangan bulat")

print("Rata-ratanya adalah: {0}".format(InputData/Perhitungan))
