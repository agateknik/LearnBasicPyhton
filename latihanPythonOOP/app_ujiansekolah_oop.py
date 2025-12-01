import random

class Soal:
    def __init__(self, pertanyaan, jawaban, jawaban_benar):
        self.pertanyaan = pertanyaan
        self.jawaban = jawaban
        self.jawaban_benar = jawaban_benar
        
        random.shuffle(self.jawaban)  #acak urutan jawaban saat objek dibuat
        
    def cek_jawaban(self, jawaban_user):
        return jawaban_user == self.jawaban_benar

class SoalUjian:
    def __init__(self, soal_asli):
        self.daftar_soal = []
        
        random.shuffle(soal_asli)  #acak urutan soal saat objek dibuat
        
        for i in range(10):
            soal = soal_asli[i]         #pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4
            data = soal.split("|")      #format jadi list [pertanyaan, jawaban1,jawaban2,jawaban3,jawaban4]
            
            pertanyaan = data[0]        #pertanyaan
            semua_jawaban = data[1]     #jawaban1,jawaban2,jawaban3,jawaban4
            
            jawaban = semua_jawaban.split(",") #buat list jawaban [jawaban1, jawaban2, jawaban3, jawaban4]
            jawaban_benar = jawaban[0]  
            
            soal = Soal(pertanyaan, jawaban, jawaban_benar)
            self.daftar_soal.append(soal)

class AplikasiUjianSekolah:
    def __init__(self, file_soal):
        soal_asli= []
        with open(file_soal, "r") as file:
            for line in file:
                soal_asli.append(line.strip())
        
        self.soal_ujian = SoalUjian(soal_asli)
    
    def run(self):
        opsi = ["A", "B", "C", "D"]
        jawaban_salah = 0
        jawaban_benar = 0
        
        for i in range(len(self.soal_ujian.daftar_soal)):
            soal = self.soal_ujian.daftar_soal[i]
            print("Pertanyaan No",i+1,":",soal.pertanyaan)
            
            print("Jawaban:")
            for j in range(len(soal.jawaban)):
                jawaban = soal.jawaban[j]
                print(opsi[j],".",jawaban)
            
            while True:
                try:    
                    jawaban_user = input("Masukkan jawaban Anda (A/B/C/D): ").upper()
                    indeks_jawaban = opsi.index(jawaban_user)   #mengubah A/B/C/D ke indeks 0/1/2/3
                    jawaban_dipilih = soal.jawaban[indeks_jawaban]
                    break
                
                except (ValueError, IndexError):
                    print("Input tidak valid. input lagi antara A/B/C/D")
            
            if soal.cek_jawaban(jawaban_dipilih):
                jawaban_benar += 1
            else:
                jawaban_salah += 1
        
        print("Ujian Selesai!")
        print("Jumlah Jawaban Benar:", jawaban_benar)
        print("Jumlah Jawaban Salah:", jawaban_salah)
        
    
if __name__ == "__main__":
    app = AplikasiUjianSekolah("bank_soal.txt")
    app.run()
    print("Terima kasih telah mengikuti ujian sekolah!")

