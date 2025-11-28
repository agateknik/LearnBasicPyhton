def ambil_soal(lokasi_file):
    soal_asli = []
    with open(lokasi_file, "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli


def buat_soal(lokasi_file):
    soal_asli = ambil_soal(lokasi_file)
    
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