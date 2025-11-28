import matematika

if __name__ == "__main__":
    x = 10
    y = 5
    print(f"hasil penjumlahan {x} + {y} = {matematika.tambah(x,y)}")
    print(f"hasil pengurangan {x} - {y} = {matematika.kurang(x,y)}")
    print(f"hasil perkalian {x} * {y} = {matematika.kali(x,y)}")
    print(f"hasil pembagian {x} / {y} = {matematika.bagi(x,y)}")
    
    print(f"nilai PI adalah: {matematika.PI}")
    print(f"dibuat oleh: {matematika.TIM_PEMBUAT}")
