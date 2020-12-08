myData = ['apel', 'rambutan', 'jeruk']
def sortStringByChar(x):
    x.sort(reverse=True, key=len)
    return x
print(sortStringByChar(myData))
