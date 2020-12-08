n = int(input('Banyak Data: '))
print()
data = []
jum = 0

for i in range(0, n):
        temp = int(input('Masukan Data: '))
        data.append(temp)
        jum += data[i]
        rata2 = jum / n
print('Rata rata = %0.2f' % rata2)
