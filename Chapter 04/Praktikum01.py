# import library
import time
import datetime

# input nama user
nama = input("Hallo... nama saya Mr. Kompie, nama Anda siapa? ")

# tampilkan nama user
print("Oh.. nama Anda", nama, ", nama yang bagus sekali.")


# kasih jeda 3 detik
time.sleep(3)

# input tahun lahir
thnLahir = int(input("BTW...  " + nama + "kamu lahir tahun berapa? "))

# kasih jeda 3 detik
time.sleep(3)

# hitung usia user 
skrg = datetime.datetime.now()
usia = skrg.year - thnLahir

# tampilkan usia
print("Hmmm...", nama,"kamu sudah", usia,"tahun ya..")

# kasih jeda 3 detik
time.sleep(3)

# tampilkan pesan sesuai range usia
if (usia > 50):
    print("Anda sudah cukup tua ya?")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
else:
    print("Oalah.. Anda masih anak-anak toh?")
    print("Jangan suka merengek-rengek minta jajan ya!!")

# kasih jeda 3 detik
time.sleep(3)

# say goodbye
print("OK.. see you later", nama, ".. senang berkenalan denganmu")
