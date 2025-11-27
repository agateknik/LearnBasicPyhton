def ambil_soal():
    soal_asli = []
    with open("bank_soal.txt", "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()
    
    import random
    #acak urutan soal
    random.shuffle(soal_asli)
    
    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i]         #pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4
        data = soal.split("|")      #format jadi list [pertanyaan, jawaban1,jawaban2,jawaban3,jawaban4]
        
        pertanyaan = data[0]        #pertanyaan
        semua_jawaban = data[1]     #jawaban1,jawaban2,jawaban3,jawaban4
        
        jawaban = semua_jawaban.split(",") #buat list jawaban [jawaban1, jawaban2, jawaban3, jawaban4]
        jawaban_benar = jawaban[0]          #jawaban benar adalah jawaban1
        
        #acak urutan jawaban
        random.shuffle(jawaban)             #jawaban diacak , contoh format [jawaban3, jawaban1, jawaban4, jawaban2]
        
        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })
    return soal_ujian

def app_ujian_sekolah():
    soal_ujian = buat_soal()
    opsi = ["A", "B", "C", "D"]
    jawaban_salah = 0
    jawaban_benar = 0
    
    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print("Pertanyaan No",i+1,":",soal["pertanyaan"])
        
        print("Jawaban:")
        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][j]
            print(opsi[j],".",jawaban)
        
        while True:
            try:    
                jawaban_user = input("Masukkan jawaban Anda (A/B/C/D): ").upper()
                indeks_jawaban = opsi.index(jawaban_user)   #mengubah A/B/C/D ke indeks 0/1/2/3
                jawaban_dipilih = soal["jawaban"][indeks_jawaban]
                break
            
            except (ValueError, IndexError):
                print("Input tidak valid. input lagi antara A/B/C/D")
            
        if jawaban_dipilih == soal["jawaban_benar"]:
                print("Jawaban Anda benar")
                jawaban_benar += 1
        else:
                print("Jawaban Anda salah")
                jawaban_salah += 1

    print("\n=== Hasil Ujian ===")
    print("Jumlah Jawaban Benar:", jawaban_benar)   
    print("Jumlah Jawaban Salah:", jawaban_salah)
    print("Skor Akhir:", jawaban_benar * 10, "dari 100")
    
        
app_ujian_sekolah()
