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
