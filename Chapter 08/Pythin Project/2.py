def dataStat(x):
    jumlahan = sum(x)
    pembagi = len(x)
    average = jumlahan/pembagi
    nilaiMin = min(x)
    nilaiMax = max(x)
    return [average, nilaiMin, nilaiMax]

a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
print(dataStat(a))
