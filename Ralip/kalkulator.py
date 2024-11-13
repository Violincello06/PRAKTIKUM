# Program Kalkulator Sederhana

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa membagi dengan nol!"

def pangkat(x, y):
    return x ** y

def mod(x, y):
    return x % y

def menu():
    print("Pilih operasi yang ingin dilakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Perpangkatan")
    print("6. Modulo (Sisa Pembagian)")
    print("7. Keluar")

def kalkulator():
    while True:
        menu()
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

        if pilihan == '7':
            print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
            break

        if pilihan in ['1', '2', '3', '4', '5', '6']:
            try:
                x = float(input("Masukkan angka pertama: "))
                y = float(input("Masukkan angka kedua: "))

                if pilihan == '1':
                    print(f"Hasil: {tambah(x, y)}")
                elif pilihan == '2':
                    print(f"Hasil: {kurang(x, y)}")
                elif pilihan == '3':
                    print(f"Hasil: {kali(x, y)}")
                elif pilihan == '4':
                    print(f"Hasil: {bagi(x, y)}")
                elif pilihan == '5':
                    print(f"Hasil: {pangkat(x, y)}")
                elif pilihan == '6':
                    print(f"Hasil: {mod(x, y)}")

            except ValueError:
                print("Input tidak valid. Silakan masukkan angka dengan benar.")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan kalkulator
kalkulator()
