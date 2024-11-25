def tampilkan_menu():
    print("\n=== Aplikasi To-Do List ===")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Hapus Tugas")
    print("4. Tandai Tugas Selesai")
    print("5. Keluar")

def tambah_tugas(todo_list):
    tugas = input("Masukkan nama tugas: ")
    todo_list.append({"tugas": tugas, "selesai": False})
    print(f"Tugas '{tugas}' berhasil ditambahkan!")

def tampilkan_tugas(todo_list):
    if not todo_list:
        print("Belum ada tugas dalam daftar.")
        return
    
    print("\nDaftar Tugas:")
    for idx, item in enumerate(todo_list, start=1):
        status = "✔" if item["selesai"] else "✘"
        print(f"{idx}. {item['tugas']} [{status}]")

def hapus_tugas(todo_list):
    tampilkan_tugas(todo_list)
    try:
        nomor = int(input("Masukkan nomor tugas yang akan dihapus: ")) - 1
        if 0 <= nomor < len(todo_list):
            tugas = todo_list.pop(nomor)
            print(f"Tugas '{tugas['tugas']}' berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def tandai_selesai(todo_list):
    tampilkan_tugas(todo_list)
    try:
        nomor = int(input("Masukkan nomor tugas yang selesai: ")) - 1
        if 0 <= nomor < len(todo_list):
            todo_list[nomor]["selesai"] = True
            print(f"Tugas '{todo_list[nomor]['tugas']}' telah ditandai selesai!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def main():
    todo_list = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_tugas(todo_list)
        elif pilihan == "2":
            tampilkan_tugas(todo_list)
        elif pilihan == "3":
            hapus_tugas(todo_list)
        elif pilihan == "4":
            tandai_selesai(todo_list)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
