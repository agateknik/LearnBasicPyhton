from post_comment import comment
import requests

def menu_post():
    
    while True:
        print("===MENU POST===")
        print("1. Tampilkan semua Post")
        print("2. Tampilkan Post berdasarkan ID")
        print("3. Kembali ke Menu Utama")

        pilihan = int(input("Pilih opsi (1-3): "))
        if pilihan == 1:
            tampilkan_semua_post()    
        elif pilihan == 2:
            post_id = int(input("Masukkan ID Post yang ingin ditampilkan: "))
            tampilkan_post_by_id(post_id)
            comment.menu_comment(post_id)    
        elif pilihan == 3:
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

def ambil_data_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        list = response.json()
        return list
    else:
        print("Gagal mengambil data post")
        return []
    
def tampilkan_semua_post():
    list_post = ambil_data_post()
    for post in list_post:
        print("==================================")
        print("ID Post:", post["id"])
        print("Judul Post:", post["title"])
        
def tampilkan_post_by_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        post = response.json()
        print("==================================")
        print("ID Post:", post["id"])
        print("Judul Post:", post["title"])
        print("Isi Post:", post["body"])
    else:
        print(f"Gagal mengambil data post dengan ID {post_id}")
