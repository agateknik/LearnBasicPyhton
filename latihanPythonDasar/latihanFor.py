print("=== Level 1: contoh for sederhana dengan list ===")
for i in (10,20,30):
    print("nilai i adalah", i)
    
print("=== Level 2: contoh for dengan range ===")
print("cetak angka dari 1 sampai 5")
for i in range(1,6):
    print(i)
print("cetak angka genap dari 2 sampai 10")
for i in range(2,11,2):
    print(i)

print("=== Level 3: contoh for dengan string ===")
for huruf in "python":
    print(huruf.upper())    

print("=== Level 4: contoh for dengan list dan operasi di dalamnya ===")
total = 0
print("contoh menjumlahkan angka di dalam list")
angka_list = [10,2,7,6]
for i in angka_list:
    total += i
print("Total penjulahan angka di list:",total)
total_range = 0
print("contoh mengalikan angka di dalam range")
for j in range(1,3):
    total_range += j
print("Total penjumlahan angka di range 1 sampai 3:",total_range)


print("=== Level 5: contoh for + if ===")
#cetak hanya angka genap dari 1 sampai 10
print("cetak angka genap")
for i in range(1,11):
    if i % 2 == 0:
        print(i)
print("sekarang cetak angka ganjil")
for i in range(1,11):
    if i % 2 != 0:
        print(i)
print("sekarang cetak kelipatan 3")
for i in range(1,31):
    if i % 3 == 0:
        print(i)
print("tampilkan yang bukan kelipatan 5")
for i in range(1,20):
    if i % 5 !=0:
        print(i)
        
print("=== Level 6: mini project ===")
print("hitung jumlah huruf vokal di dalam sebuah kalimat")
kalimat = input("masukkan kalimat: ")
jumlah_vokal = 0
for v in kalimat:
    if v.lower() in "aiueo":
        jumlah_vokal +=1
print("jumlah huruf vokal di dalam kalimat adalah:",jumlah_vokal)

print("TANTANGAN LANGSUNG")
print("tampilkan bintang segitiga siku-siku")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print() 
print("tampilkan bintang segitiga terbalik")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print("buat list baru dengan kuadrat angka dari list lama")
list_awal=[2,3,4,5]
list_kuadrat= []
for i in list_awal:
    list_kuadrat.append(i**2)
print("list awal:",list_awal)
print("list kuadrat:",list_kuadrat)

print("=== Buat tabel perkalian 1-5 ===")
for i in range(1,6):
    for j in range(1,6):
        hasil = i*j
        print(f"{i} x {j} = {hasil}")
    print("----------")
