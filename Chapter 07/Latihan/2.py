NamaFile = str(input("Masukkan Nama File: "))

try:
    selesai = False
    while not(selesai):
        TambahData = str(input("Data yang mau ditambahkan: "))
        file = open(NamaFile, "a")
        file.write("{0}\n".format(TambahData))
        file.close()
        choice = None
        while choice not in("y","n"):
            choice = str(input("Mau lagi (y/n)?: "))
            if(choice == "y"):
                selesai = False
            elif(choice == "n"):
                selesai = True
            else:
                print("Mohon masukkan pilihan (y/n)")

except FileNotFoundError:
    print("File Tidak Ditemukan... / Masukan Nama File dengan Tepat")
