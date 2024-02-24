# Program untuk mencetak nilai tengah dari tiga buah nilai yang diinput.
import os
import time

def input_bilangan():
    while True:
        try:
            input_bilangan = input("Input 3 Angka: ")
            bilangan1, bilangan2, bilangan3 = map(int, input_bilangan.split())
            # kondisi untuk antisipasi ketika terdapat dua atau lebih bilangan yang bernilai sama
            if bilangan1 == bilangan2 or bilangan1 == bilangan3 or bilangan2 == bilangan3:
                raise ValueError("Bilangan-bilangan tersebut tidak boleh sama.")
            return bilangan1, bilangan2, bilangan3
        except ValueError as e:
            print("Error:", e, "\n")

def cari_nilai_tengah(bilangan1, bilangan2, bilangan3):
    if bilangan1 < bilangan2 < bilangan3 or bilangan3 < bilangan2 < bilangan1:
        return bilangan2
    elif bilangan2 < bilangan1 < bilangan3 or bilangan3 < bilangan1 < bilangan2:
        return bilangan1
    else:
        return bilangan3

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+========================================+")
    print("| NIM: 2311601526                        |")
    print("| Nama: Rizky Ardiansyah                 |")
    print("| Program untuk mencetak nilai tengah    |")
    print("| dari tiga buah nilai yang diinput      |")
    print("+========================================+\n")
    bilangan1, bilangan2, bilangan3 = input_bilangan()
    nilai_tengah = cari_nilai_tengah(bilangan1, bilangan2, bilangan3)
    print("Angka 1: ", bilangan1)
    print("Angka 2: ", bilangan2)
    print("Angka 3: ", bilangan3)
    print("Nilai tengah adalah:", nilai_tengah, "\n")

    ulangi = input("Lanjut? (y/t): ")
    if ulangi.lower() != 'y':
        print("Bye~")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        break


