from random import randint
# GAME TEBAK ANGKA
print("Hai.. nama saya Mr. Quiz, saya telah memilih bilangan bulat secara acak antara 0 sampai dengan 100, silakan ditebak ya!")
angkaYangHarusDitebak = randint(0,100)
skorMula = 100
while skorMula != 0:
 angkaTebakan = int(input("Tebakan Anda : "))
 if(angkaTebakan == angkaYangHarusDitebak):
    print("Yup, tebakan anda benar\n")
    print("Skor Anda: {0}".format(skorMula))
    break
 elif(angkaTebakan > angkaYangHarusDitebak):
    print("Maaf, bilangan tebakan anda terlalu besar")
    skorMula -= 2
 elif(angkaTebakan < angkaYangHarusDitebak):
    print("Maaf, bilangan tebakan anda terlalu kecil")
    skorMula -= 2
