PI = 3,14
TIM_PEMBUAT = "Tim Matematika"

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan."

if __name__ == "__main__":
    print("Ini adalah module bukan program utama, silahkan run file main.py")

