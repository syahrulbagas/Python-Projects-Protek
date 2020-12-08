from random import randint
# GAME TEBAK ANGKA
print("Hai.. nama saya Mr. Quiz, saya telah memilih bilangan bulat secara acak antara 0sampai dengan 100, silakan ditebak ya!")
angkaYangHarusDitebak = randint(0,100)
while True:
    angkaTebakan = int(input("Tebakan Anda : "))
    if(angkaTebakan == angkaYangHarusDitebak):
        print("Yup, tebakan anda benar")
        break
    elif(angkaTebakan > angkaYangHarusDitebak):
        print("Maaf, bilangan tebakan anda terlalu besar")
    elif(angkaTebakan < angkaYangHarusDitebak):
        print("Maaf, bilangan tebakan anda terlalu kecil")
