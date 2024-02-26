# UAS


---

## Soal 1
![Image Description](https://raw.githubusercontent.com/rainerhosch/Budiluhur/main/Matrikulasi/Perancangan%20dan%20Analisa%20Algoritma/UAS/soal-1.png)

```python
def main():
    jarak_titikA_titikB = 1000
    kecepatan_awal_ali = 2 #2 per detik
    kecepatan_awal_badu = 3 #3 per detik
    rate_akselerasi = 0.1 #0.1 per detik
    interval_waktu = 10 #interval waktu untuk variabel perubahan kecepatan setiap 10 detik

    posisi_ali = 0
    posisi_badu = 0
    waktu = 0

    while posisi_ali < jarak_titikA_titikB and posisi_badu < jarak_titikA_titikB:
        posisi_ali = hitung_posisi(waktu, kecepatan_awal_ali, rate_akselerasi, interval_waktu)
        posisi_badu = kecepatan_awal_badu * (waktu / 60) # 60 detik = 1 menit
        waktu += 1

        if posisi_badu >= posisi_ali:
            break

    waktu_jam = waktu // 3600
    waktu_menit = (waktu % 3600) // 60
    waktu_detik = (waktu % 3600) % 60

    print(f"Badu dapat mendahului Ali pada pukul {waktu_jam:02d}:{waktu_menit:02d}:{waktu_detik:02d}")


def hitung_posisi(waktu, initial_speed, rate_akselerasi, interval_waktu):
    kecepatan_now = initial_speed + rate_akselerasi * (waktu // interval_waktu)
    jarakPerjalanan = (initial_speed + kecepatan_now) / 2 * waktu
    return jarakPerjalanan


if __name__ == "__main__":
    print("+========================================+")
    print("| NIM : 2311601526                       |")
    print("| Nama: Rizky Ardiansyah                 |")
    print("| UAS : SOAL 1                           |")
    print("+========================================+\n")
    main()
```
## Hasil program soal 1
![Image Description](<https://raw.githubusercontent.com/rainerhosch/Budiluhur/main/Matrikulasi/Perancangan%20dan%20Analisa%20Algoritma/UAS/hasil-soal1.png>)

---

## Soal 2
![Image Description](https://raw.githubusercontent.com/rainerhosch/Budiluhur/main/Matrikulasi/Perancangan%20dan%20Analisa%20Algoritma/UAS/soal-2.png)

```python
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
```
## Hasil program soal 2
![Image Description](<https://raw.githubusercontent.com/rainerhosch/Budiluhur/main/Matrikulasi/Perancangan%20dan%20Analisa%20Algoritma/UAS/hasil-soal2.png>)