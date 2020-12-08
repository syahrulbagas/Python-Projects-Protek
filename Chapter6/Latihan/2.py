def starFormation1(n):
    i = 0
    while (i<n):
        j = 0
        while (j <= i):
            print('*', end='')
            j +=1
            print('')
            i += 1

def starFormation2(n):
    i = 0
    while (i<n):
        j = 0
        while (j > i):
            print('*', end='')
            j -=1
            print('')
            i += 1

def starFormation(a):
    formasi1 = a //2
    formasi2 = (a // 2) +1
    starFormation1(formasi1)
    starFormation2(formasi2)

banyakBintang = int(input('Tentukan Banyak BAris: '))
starFormation(banyakBintang)

