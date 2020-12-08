NamaFile = str(input("Masukkan Nama File: "))

try:
    FileOpen = open(NamaFile, "r")
    print(FileOpen.read())
except FileNotFoundError:
    print("File Tidak Ditemukan... / Masukan Nama File dengan Tepat")
