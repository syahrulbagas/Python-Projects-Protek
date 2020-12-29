def Formasi(n):
    a = 0
    b = -1
    for a in range ((n//2) + 1):
        a += 1
        b += 2
        bil = '*' * b
        print (bil.center(n+n))

    for a in range (((n//2) + 1), (n+1)):
        a += 1
        b -= 2
        bil = '*' * b
        print (bil.center(n+n))

Formasi (7)
