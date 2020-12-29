import random
def shuffleString(kata, n):
    listKata = []
    while (len(listkata) < n):
        acakKata = random.sample(kata, len(kata))
        acak = ''.join(acakKata)
        if(acak not in listkata):
            listKata.append(acak)

    print(listKata)

shuffleString('kuma', 10)
