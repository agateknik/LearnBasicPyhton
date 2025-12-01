class Aset:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        
class AsetKendaraan(Aset):
    def __init__(self, kode, nama, harga, jenis_kendaraan, tahun):
        super().__init__(kode, nama, harga)
        self.jenis_kendaraan = jenis_kendaraan
        self.tahun = tahun
        
class AsetElektronik(Aset):
    def __init__(self, kode, nama, harga, tipe_elektronik, garansi):
        super().__init__(kode, nama, harga)
        self.tipe_elektronik = tipe_elektronik
        self.garansi = garansi
    
class AsetTanahBangunan(Aset):
    def __init__(self, kode, nama, harga, lokasi, luas):
        super().__init__(kode, nama, harga)
        self.lokasi = lokasi
        self.luas = luas
            
class DaftarAset:
    def __init__(self):
        self.daftar_aset = []
            
    def ambil_aset(self, kode):
        for aset in self.daftar_aset:
            if aset.kode == kode:
                return aset
        return None
    
    def hapus_aset(self, kode):
        for i, aset in enumerate(self.daftar_aset):
            if aset.kode == kode:
                del self.daftar_aset[i]
                return True   
        return False
            
class AplikasiAsetManajemen:
    def __init__(self):
        self.daftar_aset = DaftarAset()
        
    def run(self):
        while True:
            print("=== Menu Aplikasi Manajemen Aset ===")
            print("1. Tambah Aset")
            print("2. Lihat Daftar Aset")
            print("3. Keluar")
                       
            pilihan = int(input("Pilih menu (1-3): "))
                
            if pilihan == 1:
                self.run_tambah_aset()
            elif pilihan == 2:
                self.run_lihat_daftar_aset()
            elif pilihan == 3:
                break   
                
            else:
                print("Input tidak valid. Masukkan angka antara 1-5.")  
                
    def run_tambah_aset(self):
        while True:
            print("Pilih Jenis Aset yang akan ditambahkan:")
            print("1. Aset Kendaraan")
            print("2. Aset Elektronik")
            print("3. Aset Tanah dan Bangunan")     
            print("4. Kembali ke Menu Utama")
               
            pilihan = int(input("Pilih jenis aset (1-4): "))
               
            if pilihan == 1:
                self.run_tambah_aset_kendaraan()
            elif pilihan == 2:
                self.run_tambah_aset_elektronik()     
            elif pilihan == 3:
                self.run_tambah_aset_tanah_bangunan()   
            elif pilihan == 4:
                break
                 
            else:   
                print("Input tidak valid. Masukkan angka antara 1-4.")
        
    def run_tambah_aset_kendaraan(self):
        print("===Tambah aset kendaraan===")
        kode = input("Masukkan kode aset: ")
        nama = input("Masukkan nama aset kendaraan: ")
        harga = int(input("Masukkan harga aset kendaraan: "))
        jenis_kendaraan = input("Masukkan jenis kendaraan: ")
        tahun = int(input("Masukkan tahun kendaraan: "))
            
        aset_kendaraan = AsetKendaraan(kode, nama, harga, jenis_kendaraan, tahun)
        self.daftar_aset.daftar_aset.append(aset_kendaraan)
        print("Aset kendaraan berhasil ditambahkan.") 
            
        
    def run_tambah_aset_elektronik(self):
        print("===Tambah aset elektronik===")
        kode = input("Masukkan kode aset: ")
        nama = input("Masukkan nama aset elektronik: ")
        harga = int(input("Masukkan harga aset elektronik: "))
        tipe_elektronik = input("Masukkan tipe elektronik: ")
        garansi = int(input("Masukkan garansi elektronik (dalam bulan): "))

        aset_elektronik = AsetElektronik(kode, nama, harga, tipe_elektronik, garansi)
        self.daftar_aset.daftar_aset.append(aset_elektronik)
        print("Aset elektronik berhasil ditambahkan.")  
        
    def run_tambah_aset_tanah_bangunan(self):
        print("===Tambah aset tanah dan bangunan===")
        kode = input("Masukkan kode aset: ")
        nama = input("Masukkan nama aset tanah dan bangunan: ")
        harga = int(input("Masukkan harga aset tanah dan bangunan: ")) 
        lokasi = input("Masukkan lokasi aset tanah dan bangunan: ")
        luas = int(input("Masukkan luas aset tanah dan bangunan (dalam m2): "))
            
        aset_tanah_bangunan = AsetTanahBangunan(kode, nama, harga, lokasi, luas)
        self.daftar_aset.daftar_aset.append(aset_tanah_bangunan)
        print("Aset tanah dan bangunan berhasil ditambahkan.")
             
    def run_lihat_daftar_aset(self):
        for aset in self.daftar_aset.daftar_aset:
            if isinstance(aset, AsetKendaraan):
                print("Aset Kendaraan")
                print("Kode:", aset.kode)
                print("Nama:", aset.nama)
                print("Harga:", aset.harga)
                print("Jenis Kendaraan:", aset.jenis_kendaraan)
                print("Tahun:", aset.tahun)
                print()

            elif isinstance(aset, AsetElektronik):
                print("Aset Elektronik")
                print("Kode:", aset.kode)
                print("Nama:", aset.nama)
                print("Harga:", aset.harga)
                print("Tipe Elektronik:", aset.tipe_elektronik)
                print("Garansi:", aset.garansi, "bulan")
                print()
                    
            elif isinstance(aset, AsetTanahBangunan):
                print("Aset Tanah dan Bangunan")
                print("Kode:", aset.kode)
                print("Nama:", aset.nama)
                print("Harga:", aset.harga)
                print("Lokasi:", aset.lokasi)
                print("Luas:", aset.luas, "m2")
                print()
        
        while True:
            print("Menu tambahan")
            print("1. Edit data aset")
            print("2. Hapus data aset")
            print("3. Kembali ke menu utama")
        
            pilihan = int(input("Pilih menu (1-3): "))
            if pilihan == 1:
                self.run_edit_aset()
            elif pilihan == 2:
                self.run_hapus_aset()
            elif pilihan == 3:
                break
            else:
                print("Input tidak valid. Masukkan angka antara 1-3.")
    
    def run_hapus_aset(self):
        kode = input("Masukkan kode aset yang akan dihapus: ")
        if self.daftar_aset.hapus_aset(kode):
            print(f"Aset dengan kode {kode} berhasil dihapus.")
        else:
            print(f"Aset dengan kode {kode} tidak ditemukan.")
            self.run_lihat_daftar_aset()
            
    def run_edit_aset(self):
        kode = input("Masukkan kode aset yang akan diedit: ")
        aset = self.daftar_aset.ambil_aset(kode)
        
        if aset is None:
            print(f"Aset dengan kode {kode} tidak ditemukan.")
            self.run_lihat_daftar_aset()
        else:
            if isinstance(aset, AsetKendaraan):
                print("Edit data aset kendaraan")
                aset.nama = input("Masukkan nama aset kendaraan: ")
                aset.harga = int(input("Masukkan harga aset kendaraan: "))
                aset.jenis_kendaraan = input("Masukkan jenis kendaraan: ")
                aset.tahun = int(input("Masukkan tahun kendaraan: "))
                print("Data aset kendaraan berhasil diubah.")
                self.run_lihat_daftar_aset()
            
            elif isinstance(aset, AsetElektronik):
                print("Edit data aset elektronik")
                aset.nama = input("Masukkan nama aset elektronik: ")
                aset.harga = int(input("Masukkan harga aset elektronik: "))
                aset.tipe_elektronik = input("Masukkan tipe elektronik: ")
                aset.garansi = int(input("Masukkan garansi elektronik (dalam bulan): "))
                print("Data aset elektronik berhasil diubah.")
                self.run_lihat_daftar_aset()
            
            elif isinstance(aset, AsetTanahBangunan):
                print("Edit data aset tanah dan bangunan")
                aset.nama = input("Masukkan nama aset tanah dan bangunan: ")
                aset.harga = int(input("Masukkan harga aset tanah dan bangunan: "))
                aset.lokasi = input("Masukkan lokasi aset tanah dan bangunan: ")
                aset.luas = int(input("Masukkan luas aset tanah dan bangunan (dalam m2): "))
                print("Data aset tanah dan bangunan berhasil diubah.")
                self.run_lihat_daftar_aset()
                    

if __name__ == "__main__":
    aplikasi = AplikasiAsetManajemen()
    aplikasi.run()
    print("Terima kasih telah menggunakan aplikasi manajemen aset.")



                    
                   