def ubahHuruf(teks, a, b):
    listkata = list (teks)
    for huruf in listkata :
    	if huruf == a :
    		listkata[listkata.index(a)]=b
    		UbahKata = ''.join(listkata)
    print (UbahKata)
    	

ubahHuruf('matematika', 'e', 's')
