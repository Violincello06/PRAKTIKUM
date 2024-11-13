#membuat fungsi dengan parameter
#fungsi dengan 1 parameter
def halo (nama) :
    print ('Halo',nama)

#fungsi dengan 2 parameter
def luas_segitiga (alas,tinggi) :
    luas = int((alas*tinggi)/2)
    print ('Luas Segitiga :',luas)

def banding (a,b) :
    if a > b :
        print ('%s > %s'%(a,b))
    else :
        print ('%s < %s'%(a,b))
#memanggil fungsi
halo ('ralip')
halo ('informatika')
print ('----------------------')
luas_segitiga (9,7)
print ('----------------------')
banding (10,20)
banding (20,10)
   