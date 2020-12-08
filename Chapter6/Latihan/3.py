def faktorial(n):
    if (n == 0):
        hasil = 1
        return hasil

    elif(n>0):
        i = 1
        for j in range(n):
            i = i * (j+1)
            hasil = i
            return hasil
        else:
            exit()

def C(a,b):
    hasil = faktorial(a)/faktorial(a-b)* faktorial(b)
    return hasil

def P(a,b):
    hasil = faktorial(a) / faktorial(a-b)
    return hasil

print('Nilai C(5,3) adalah {0}'.format(C(5,3)))
print('Nilai P(10,7) adalah {0}'.format(C(10,7)))
