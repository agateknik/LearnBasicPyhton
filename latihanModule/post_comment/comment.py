import requests

def menu_comment(post_id):
    while True:
        print("===MENU COMMENT===")
        print("1. Tampilkan semua Comment untuk Post ID", post_id)
        print(f"2. Tampilkan Comment berdasarkan ID comment dari {post_id}")
        print("3. Kembali ke Menu Post")

        pilihan = int(input("Pilih opsi (1-3): "))
        if pilihan == 1:
            tampilkan_semua_comment(post_id)    
        elif pilihan == 2:
            comment_id = int(input(f"Masukkan ID Comment dari Post {post_id} yang ingin ditampilkan: "))
            tampilkan_comment_by_id(post_id, comment_id)    
        elif pilihan == 3:
            print("Kembali ke Menu Post.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

def ambil_data_comment(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    if response.status_code == 200:
        comments = response.json()
        return comments
    else:
        print("Gagal mengambil data comment")
        return []

def tampilkan_semua_comment(post_id):
    list_comment = ambil_data_comment(post_id)
    for comment in list_comment:
        print("==================================")
        print("ID Comment:", comment["id"])
        print("Nama Commenter:", comment["name"])
        print("Email Comenter:", comment["email"])
    
def tampilkan_comment_by_id(post_id, comment_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/comments/{comment_id}")
    if response.status_code == 200:
        comment = response.json()
        if comment["postId"] == post_id:
            print("==================================")
            print("ID Comment:", comment["id"])
            print("Nama Commenter:", comment["name"])
            print("Email Comenter:", comment["email"])
            print("Isi Comment:", comment["body"])
        else:
            print(f"Comment ID {comment_id} tidak terdapat di Post ID {post_id}")
    else:
        print("Gagal mengambil data")


