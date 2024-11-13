#variabel
a = 1
def fungsi1():
    print (a)
def fungsi2():
    #variabel lokal
    a = 2
    print (a)
def fungsi3():
    #variabel lokal
    a = 3
    print (a)
def fungsi4():
    global a
    #variabel lokal
    a = 4
    print (a)


print ('Variabel Global=',a)
fungsi1()
print('=====================')
print ('Variabel Global=',a)
fungsi2()
print('=====================')
print('Variabel Global=',a)
fungsi3()
print ('====================')
print ('Variabel Global=',a)
fungsi4()
print ('====================')
print ('Variabel Global=',a)