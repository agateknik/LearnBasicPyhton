import json

"""
__documentation__
https://docs.python.org/3/library/json.html#module-json
"""

data_siswa =[{
    "nama": "Andi",
    "umur": 20,
    "alamat": "Jl. Merdeka No. 123",
    "hobi": ["membaca", "menulis", "menggambar"]
}]

text_json = json.dumps(data_siswa)
print("text json:", text_json)

json_string = '{"nama": "Ani", "umur": 22, "alamat": "Bekasi", "hobi": ["membaca"]   }'
data_json = json.loads(json_string)
print("data json baru:", data_json)

#tambah data_iswa dari data json    
print("data siswa lama:", data_siswa)
data_siswa.append(data_json)
print("data siswa terbaru:", data_siswa)