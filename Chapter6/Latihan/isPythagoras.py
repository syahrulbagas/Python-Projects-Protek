def pythagoras (a, b, c):
    if(a**2 + b**2 == c**2):
        return True
    else:
        return False

A=(int(input('Masukkan Nilai A:')))
B=(int(input('Masukkan Nilai B:')))
C=(int(input('Masukkan Nilai C:')))

print('a={0}, b={1}, c={2} {3}'. format(A, B, C, pythagoras(A, B, C)))
