#module random
import random

#cetak angka secara random dengan range
print("cetak angka secara random dengan range", random.randint(1, 10))
print("cetak angka secara random dengan range", random.randint(1, 100 ))

#menggunakan fungsi choice
list_angka = [1, 2, 3, 4, 5]
print("cetak angka secara random dengan choice:", random.choice(list_angka))

list_buah = ["apel", "pisang", "jeruk", "mangga"]
print("cetak nama buah secara acak:", random.choice(list_buah) )

"""
untuk contoh function lain dari library random bisa ke: 
https://docs.python.org/3/library/random.html#module-random

"""