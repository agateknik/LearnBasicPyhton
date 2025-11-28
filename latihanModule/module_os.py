import os

"""_documentation
https://docs.python.org/3/library/os.html#module-os
"""

#informasi dikrektori, sistem
print("direktori kerja saat ini", os.getcwd())
print("nama sistem operasi:", os.name)

#cek apakah file/direktori ada
print("file module_datetime.py ada:", os.path.exists("module_datetime.py"))
print("direktori latihanModule ada:", os.path.exists("latihanModule"))

#informasi file 
if os.path.exists("module_datetime.py"):
    print("informasi dari file:", os.path.basename("module_datetime.py"))
    print("============================================")
    print("berada di direktori:",os.path.abspath("module_datetime.py"))
    print("ukuran file:", os.path.getsize("module_datetime.py"))
   
#path operations
print("============================================")
print("path operations")
file_path = "Users/zenbook duo/Documents/Python Scripts/ByProgrammerNow/latihanModule/module_datetime.py"
print("Direktori:", os.path.dirname(file_path))
print("Nama file:", os.path.basename(file_path))
print("Nama file tanpa ekstensi:", os.path.splitext(file_path)[0])
print("Ekstensi file:", os.path.splitext(file_path)[1])

