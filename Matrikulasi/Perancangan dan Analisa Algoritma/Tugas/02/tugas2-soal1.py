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
