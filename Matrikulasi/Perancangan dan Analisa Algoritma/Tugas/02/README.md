# Tugas 02

---

## Soal 1

- Seseorang berangkat pukul 08 : 52 : 45 ( pukul 08 lewat 52 menit 45 detik )
- tiba ditujuan setelah 5000 detik kemudian.
- Susun program untuk menghitung dan mencetak pukul berapa ( jam : menit : detik ) dia tiba ditempat tujuan.

```python


from datetime import datetime, timedelta

# Waktu keberangkatan sesuai soal 1 yaitu pukul 08 lewat 52 menit 45 detik
str_waktu_keberangkatan="08:52:45"
waktu_keberangkatan = datetime.strptime(str_waktu_keberangkatan, '%H:%M:%S')
print("Seorang memulai perjalanan pada pukul {} lewat {} menit {} detik".format(waktu_keberangkatan.hour, waktu_keberangkatan.minute, waktu_keberangkatan.second))

# Lama waktu perjalanan hingga sampai ditempat tujuan (dalam detik)
waku_perjalanan = 5000
waktujalan = datetime.strptime(str(timedelta(seconds=waku_perjalanan)), '%H:%M:%S')
print("Jika lama waktu perjalanannya adalah ",waku_perjalanan," detik, atau {} jam lewat {} menit {} detik".format(waktujalan.hour, waktujalan.minute, waktujalan.second))
# Perhitungan waktu kedatangan atau waktu tiba ditempat tujuan
waktu_tiba = waktu_keberangkatan + timedelta(seconds=waku_perjalanan)


# Cetak waktu kedatangan dalam format (jam : menit : detik)
print("Maka pada pukul: ( {}:{}:{}".format(waktu_tiba.hour, waktu_tiba.minute, waktu_tiba.second), ") orang tersebut akan tiba ditempat tujuan.")
# print("Maka orang tersebut akan tiba pada pukul: \n{}:{}:{}".format(waktu_tiba.hour, waktu_tiba.minute, waktu_tiba.second), "Pukul {} lewat {} menit {} detik".format(waktu_tiba.hour, waktu_tiba.minute, waktu_tiba.second))

```

## Hasil program soal 1

![Image Description](<https://raw.githubusercontent.com/rainerhosch/Budiluhur/main/Matrikulasi/Perancangan%20dan%20Analisa%20Algoritma/Tugas/02/Tugas2-soal1(konsol).png>)

---

## Soal 2

- Seseorang berangkat pukul 08 : 52 : 45 ( pukul 08 lewat 52 menit 45 detik ) ,
- tiba ditujuan pukul : 12 : 15 : 10.
- Susun program untuk menghitung dan mencetak berapa jam, berapa menit dan berapa detik waktu yang dia habiskan dalam perjalanan.

```python
from datetime import datetime, timedelta

# Waktu keberangkatan sesuai soal 2 yaitu pukul 08 lewat 52 menit 45 detik
str_waktu_keberangkatan="08:52:45"
waktu_keberangkatan = datetime.strptime(str_waktu_keberangkatan, '%H:%M:%S')

# waktu kedatangan atau waktu tiba ditujuan pukul: 12:15:10.
waktu_tiba = datetime.strptime('12:15:10', '%H:%M:%S')

print("Seorang berangkat pukul {}:{}:{}".format(waktu_keberangkatan.hour, waktu_keberangkatan.minute, waktu_keberangkatan.second))
print("(pukul {} lewat {} menit {} detik".format(waktu_keberangkatan.hour, waktu_keberangkatan.minute, waktu_keberangkatan.second),"), \nDan tiba ditujuan pukul: {}:{}:{}".format(waktu_tiba.hour, waktu_tiba.minute, waktu_tiba.second),"\n")

# hitung durasi waktu perjalanan
durasi_waktu_perjalanan = waktu_tiba - waktu_keberangkatan

# Mengkonversi durasi waktu perjalanan ke dalam format jam, menit, dan detik
jam, remainder = divmod(durasi_waktu_perjalanan.total_seconds(), 3600)
menit, detik = divmod(remainder, 60)

# Cetak durasi perjalanan
print("Waktu yang dihabiskan dalam perjalanan: {} jam, {} menit, {} detik".format(int(jam), int(menit), int(detik)))
```

## Hasil program soal 2

![Image Description](<https://raw.githubusercontent.com/rainerhosch/Budiluhur/main/Matrikulasi/Perancangan%20dan%20Analisa%20Algoritma/Tugas/02/Tugas2-soal2(konsol).png>)
