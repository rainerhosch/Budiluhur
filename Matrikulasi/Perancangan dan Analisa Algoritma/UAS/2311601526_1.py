def main():
    kordinat_ali = 0 #posisi awal ali
    kordinat_badu = 0 #posisi awal badu
    waktu = 0 #variabel posisi waktu awal
    
    jarak_titikA_titikB = 1000 #jarak titik a dan titik b
    kecepatan_awal_ali = 2 #2 per detik
    kecepatan_awal_badu = 3 #3 per detik
    rate_akselerasi = 0.1 #0.1 per detik
    _intv = 10 #10 dtik intervl wktu

    while kordinat_ali < jarak_titikA_titikB and kordinat_badu < jarak_titikA_titikB:
        kordinat_ali = hitung_posisi(kecepatan_awal_ali, rate_akselerasi, _intv, waktu)
        kordinat_badu = kecepatan_awal_badu * (waktu / 60) # 60 detik = 1 menit
        waktu += 1

        if kordinat_badu >= kordinat_ali:
            break

    jam = waktu // 3600 #menghitung format jam
    menit = (waktu % 3600) // 60 #menghitung format menit
    detik = (waktu % 3600) % 60 #menghtng ke dtik

    print("Badu dapat mendahului Ali pada pukul {jam:02d}:{menit:02d}:{detik:02d}")


def hitung_posisi(kecepatan_awal_ali, rate_akselerasi, _intv, waktu):
    kecepatan_now = initial_speed + rate_akselerasi * (waktu // _intv)
    jarakPerjalanan = (initial_speed + kecepatan_now) / 2 * waktu
    return jarakPerjalanan


if __name__ == "__main__":
    print("+========================================+")
    print("| NIM : 2311601526                       |")
    print("| Nama: Rizky Ardiansyah                 |")
    print("| UAS : SOAL 1                           |")
    print("+========================================+\n")
    main()
