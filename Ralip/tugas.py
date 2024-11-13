# Fungsi untuk konversi Celcius ke Reamur
def celcius_ke_reamur(celcius):
    return (4 / 5) * celcius

# Fungsi untuk konversi Celcius ke Fahrenheit
def celcius_ke_fahrenheit(celcius):
    return (9 / 5) * celcius + 32

# Fungsi untuk konversi Celcius ke Kelvin
def celcius_ke_kelvin(celcius):
    return celcius + 273.15

# Input suhu dalam Celcius
celcius = float(input("Masukkan suhu dalam Celcius: "))

# Menghitung konversi suhu
reamur = celcius_ke_reamur(celcius)
fahrenheit = celcius_ke_fahrenheit(celcius)
kelvin = celcius_ke_kelvin(celcius)

# Menampilkan hasil konversi
print(f"Suhu {celcius}°C dalam skala Reamur: {reamur}°R")
print(f"Suhu {celcius}°C dalam skala Fahrenheit: {fahrenheit}°F")
print(f"Suhu {celcius}°C dalam skala Kelvin: {kelvin} K")
