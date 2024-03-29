# Tugas 02

---

## Soal 1

- Seseorang berangkat pukul 08 : 52 : 45 ( pukul 08 lewat 52 menit 45 detik )
- tiba ditujuan setelah 5000 detik kemudian.
- Susun program untuk menghitung dan mencetak pukul berapa ( jam : menit : detik ) dia tiba ditempat tujuan.

```python
from datetime import datetime, timedelta

str_wkt="08:52:45" #set wktu brangkat 
wktBerangkat = datetime.strptime(str_wkt, '%H:%M:%S') #splt string wktu
print("Seorang memulai perjalanan pada pukul {} lewat {} menit {} detik".format(wktBerangkat.hour, wktBerangkat.minute, wktBerangkat.second))

# htung waktu perjalanan s/d  tujuan (dalam detik)
waku_perjalanan = 5000 #dlm dtik
wtkJln = datetime.strptime(str(timedelta(seconds=waku_perjalanan)), '%H:%M:%S')
print("Jika lama waktu perjalanannya adalah ",waku_perjalanan," detik, atau {} jam lewat {} menit {} detik".format(wtkJln.hour, wtkJln.minute, wtkJln.second))
# klkulasi waktu kedatangan atau waktu tiba ditempat tujuan
waktu_tiba = wktBerangkat + timedelta(seconds=waku_perjalanan)


# Tmpilkn wkt kedatangan dalam format (jam : menit : detik)
print("Maka pada pukul: ( {}:{}:{}".format(waktu_tiba.hour, waktu_tiba.minute, waktu_tiba.second), ") orang tersebut akan tiba ditempat tujuan.")
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

#Wkt berangkat sesuai soal 2 
strWktBerangkat="08:52:45"
wktBrangkat = datetime.strptime(strWktBerangkat, '%H:%M:%S')

#set wtk dtang atau waktu tiba ditujuan pukul: 12:15:10. 
wktTiba = datetime.strptime('12:15:10', '%H:%M:%S')

print("Seorang berangkat pukul {}:{}:{}".format(wktBrangkat.hour, wktBrangkat.minute, wktBrangkat.second))
print("(pukul {} lewat {} menit {} detik".format(wktBrangkat.hour, wktBrangkat.minute, wktBrangkat.second),"), \nDan tiba ditujuan pukul: {}:{}:{}".format(wktTiba.hour, wktTiba.minute, wktTiba.second),"\n")

# kalklasi wkt perjalanan
wtkPrjalanan = wktTiba - wktBrangkat

# knversi lama wkt perjalanan ke dalam format jam, menit, dan detik
jam, remainder = divmod(wtkPrjalanan.total_seconds(), 3600)
menit, detik = divmod(remainder, 60)

# Cetak durasi perjalanan
print("Waktu yang dihabiskan dalam perjalanan: {} jam, {} menit, {} detik".format(int(jam), int(menit), int(detik)))
```

## Hasil program soal 2

![Image Description](<https://raw.githubusercontent.com/rainerhosch/Budiluhur/main/Matrikulasi/Perancangan%20dan%20Analisa%20Algoritma/Tugas/02/Tugas2-soal2(konsol).png>)
