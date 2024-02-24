import os
import time

def input_bilangan():
    while True:
        try:
            input_bilangan = input("Input 3 Angka: ")
            bilangan1, bilangan2, bilangan3 = map(int, input_bilangan.split())
            return bilangan1, bilangan2, bilangan3
        except ValueError as e:
            print("Error:", e, "\n")

def cek_jenis_segitiga(bilangan1, bilangan2, bilangan3):
    if bilangan1 == bilangan2 and bilangan1 == bilangan3 :
        return 'Sama Sisi'
    elif bilangan1 == bilangan2 or bilangan1 == bilangan3 or bilangan2 == bilangan3:
        return 'Sama Kaki'
    else:
        return 'Sembarang'

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+========================================+")
    print("| NIM: 2311601526                        |")
    print("| Nama: Rizky Ardiansyah                 |")
    print("| Program untuk mencetak jenis segitiga  |")
    print("| dari tiga panjang sisi yang diinput    |")
    print("+========================================+\n")
    bilangan1, bilangan2, bilangan3 = input_bilangan()
    jenis_segitiga = cek_jenis_segitiga(bilangan1, bilangan2, bilangan3)
    print("Angka 1: ", bilangan1)
    print("Angka 2: ", bilangan2)
    print("Angka 3: ", bilangan3)
    print("Segitiga ", jenis_segitiga, "\n")

    ulangi = input("Lanjut? (y/t): ")
    if ulangi.lower() != 'y':
        print("Bye~")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        break