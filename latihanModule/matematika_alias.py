import matematika as math

if __name__ == "__main__":
    print("=====Program perkalian tidak boleh 0=====")
    while True:
        try:
            angka1 = int(input("masukkan angka pertama:"))
            angka2 = int(input("masukkan angka kedua:"))
            if angka1 == 0 or angka2 == 0:
                print("Angka tidak boleh 0, silakan coba lagi.")
            else:
                break
        except ValueError:
            print("Input harus berupa angka dan bilangan bulat. Silakan coba lagi.")
    hasil = math.kali(angka1, angka2)
    print(f"Hasil perkalian {angka1} * {angka2} = {hasil}")