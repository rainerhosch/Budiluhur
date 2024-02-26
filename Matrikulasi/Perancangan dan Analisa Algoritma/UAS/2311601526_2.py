def main():
    jarak_titikA_titikB = 1000 #jarak titik A dan titik B dalam satuan meter
    kecepatan_ali = 2 #kecepatan awal ali 2m per detik
    kecepatan_badu = 3 #kecepatan awal badu 3m per detik
    rate_akselerasi = 0.1 #variabel rate penambahan akselerasi 0.1m per detik
    waktu = 0

    posisi_ali = 0
    posisi_badu = jarak_titikA_titikB

    #looping jika posisi ali lebih kecil dari badu
    while posisi_ali < posisi_badu: 
        posisi_ali += kecepatan_ali
        kecepatan_ali += rate_akselerasi
        posisi_badu -= kecepatan_badu
        waktu += 1

    # Pada detik keberapa Ali dan Badu berpapasan
    print("Ali dan Badu akan berpapasan, pada detik ke", waktu, "setelah pukul 8.")

    # Jarak Badu dengan titik B setelah berpapasan
    print("Jarak Badu dengan titik B setelah berpapasan Ali adalah:", posisi_badu, "meter.")

if __name__ == "__main__":
    print("+========================================+")
    print("| NIM : 2311601526                       |")
    print("| Nama: Rizky Ardiansyah                 |")
    print("| UAS : SOAL 2                           |")
    print("+========================================+\n")
    main()
