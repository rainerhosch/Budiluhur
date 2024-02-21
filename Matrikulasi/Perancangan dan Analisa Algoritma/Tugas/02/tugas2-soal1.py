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
