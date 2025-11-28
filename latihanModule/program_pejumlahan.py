from matematika import tambah

if __name__ == "__main__":
    print("Program Penjumlahan Dua Angka")
    while True:
        try:
            angka1 = int(input("masukkan angka pertama:"))
            break
        except ValueError:
            print("Input harus berupa angka dan bilangan bulat. Silakan coba lagi.")

    while True:
        try:
            angka2 = int(input("masukkan angka kedua:"))
            break
        except ValueError:
            print("Input harus berupa angka dan bilangan bulat. Silakan coba lagi.")

    hasil = tambah(angka1, angka2)
    print(f"Hasil penjumlahan {angka1} + {angka2} = {hasil}")
    