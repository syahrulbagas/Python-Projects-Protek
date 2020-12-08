def nilaiakhir(nilaimhs):
    n = 0 
    for i in nilaimhs:
        MID = i.get('mid')
        UAS = i.get('uas')
        hasilakhir = (MID + 2*UAS)/3
        
        if(hasilakhir > n):
            n = hasilakhir
            real= {}
            real['nim'] = i.get('nim')
            real['nama'] = i.get('nama')
    return real

nilaimhs = [{'nim' : 'A01','nama': 'Amir','mid' : 50,'uas' : 80},
            {'nim' : 'A02','nama': 'Budi','mid' : 40,'uas' : 90},
            {'nim' : 'A03','nama': 'Cici','mid' : 50,'uas' : 50},
            {'nim' : 'A04','nama': 'Dedi','mid' : 20,'uas' : 30},
            {'nim' : 'A05','nama': 'Fifi','mid' : 70,'uas' : 40}]

done = nilaiakhir(nilaimhs)
print('Selamat, \nMahasiswa yang memiliki nilai akhir tertinggi adalah saudara {0} dengan NIM {1} '.format(done['nama'], done['nim']))
