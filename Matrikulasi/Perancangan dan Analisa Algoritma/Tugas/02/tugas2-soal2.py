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