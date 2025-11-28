import datetime

"""
Dokumentasi bisa liat di:
https://docs.python.org/3/library/datetime.html#module-datetime    
"""

#cetak tanggal dan waktu sekarang
hari_ini = datetime.datetime.now()
print("tanggal dan waktu sekarang:", hari_ini)

tanggal_hari_ini = datetime.date.today()
print("Sekarang tanggal", tanggal_hari_ini)

jam_saat_ini = datetime.datetime.now().time()
print("jam saat ini:", jam_saat_ini)

#membuat tanggal dan waktu tertentu
anniversary = datetime.date(2018, 12, 1)
print("tanggal anniversary:", anniversary)

waktu_tertentu = datetime.datetime(2018, 12, 1, 19, 00, 0)
print("waktu tertentu:", waktu_tertentu)

#mencetak keterangan waktu dengan format

#format indonesia
print("Cetak waktu dalam format Id")
print("============================================")
tanggal_indonesia_format = hari_ini.strftime("%d %B %Y")
format_panjang_id = hari_ini.strftime("%A, %d %B %Y")
print("tanggal indonesia format:", tanggal_indonesia_format)
print("dalam format panjang id:", format_panjang_id)


