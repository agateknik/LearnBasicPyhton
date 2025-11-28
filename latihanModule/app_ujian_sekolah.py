from ujian_sekolah import app

lokasi_file = "C:/Users/zenbook duo/Documents/Python Scripts/byPZN/latihanPythonDasar/bank_soal.txt" 

if __name__ == "__main__": 
        soal_ujian = app.buat_soal(lokasi_file)
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