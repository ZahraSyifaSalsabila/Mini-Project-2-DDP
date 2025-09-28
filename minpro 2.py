import maskpass # type: ignore
from prettytable import PrettyTable # type: ignore

print("Nama: Zahra Syifa Salsabila")
print("Kelas: B")
print("Tugas: Mini Project DDP")


data_kegiatan = []

data_user = {
    "mia": "12345",
    "zahra": "67890",
    "sasa": "111213",
    "zulfa": "141516",
    "kiki": "171819"
}

def login():
    print("\n LOGIN ")
    try:
        username = input("Username: ")
        password = maskpass.askpass(prompt="Password: ", mask="*")

        if username in data_user and data_user[username] == password:
            print("Login berhasil!")
            return username
        else:
            print("Login gagal, coba lagi.")
            return None
    except Exception as e:
        print("Terjadi error saat login:", e)
        return None


def pilih_role():
    print("\n PILIH ROLE ")
    print("1. Ketua")
    print("2. Sekretaris")
    print("3. Anggota")
    pilihan = input("Masukkan nomor role: ")

    if pilihan == "1":
        return "Ketua"
    elif pilihan == "2":
        return "Sekretaris"
    elif pilihan == "3":
        return "Anggota"
    else:
        return None


def tambah_kegiatan():
    try:
        kegiatan = input("Masukkan kegiatan: ")
        lokasi = input("Masukkan lokasi: ")
        tanggal_dan_waktu = input("Masukkan tanggal dan waktu: ")

        if kegiatan == "" or lokasi == "" or tanggal_dan_waktu == "":
            print("Semua data harus diisi!")
            return

        data_kegiatan.append([kegiatan, lokasi, tanggal_dan_waktu])
        print("Data berhasil ditambahkan!")
    except Exception as e:
        print("Terjadi error saat menambah data:", e)


def tampilkan_kegiatan(data_kegiatan):
    if len(data_kegiatan) == 0:
        print("Data kosong.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Kegiatan", "Lokasi", "Tanggal & Waktu"]

        for i, kegiatan in enumerate(data_kegiatan, start=1):
            tabel.add_row([i, kegiatan[0], kegiatan[1], kegiatan[2]])

        print(tabel)


def update_data():
    if len(data_kegiatan) == 0:
        print("Data kosong.")
        return
    tampilkan_kegiatan(data_kegiatan)
    try:
        index = int(input("Pilih nomor data yang mau diupdate: ")) - 1
        if 0 <= index < len(data_kegiatan):
            print("Masukkan data baru:")
            kegiatan_baru = input(f"Nama kegiatan [{data_kegiatan[index][0]}]: ")
            lokasi_baru = input(f"Lokasi [{data_kegiatan[index][1]}]: ")
            tanggal_dan_waktu_baru = input(f"Tanggal & Waktu [{data_kegiatan[index][2]}]: ")

            if kegiatan_baru == "": kegiatan_baru = data_kegiatan[index][0]
            if lokasi_baru == "": lokasi_baru = data_kegiatan[index][1]
            if tanggal_dan_waktu_baru == "": tanggal_dan_waktu_baru = data_kegiatan[index][2]

            data_kegiatan[index] = [kegiatan_baru, lokasi_baru, tanggal_dan_waktu_baru]
            print("Data berhasil diupdate!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")


def hapus_data():
    if len(data_kegiatan) == 0:
        print("Data kosong.")
        return
    tampilkan_kegiatan(data_kegiatan)
    try:
        index = int(input("Pilih nomor data yang mau dihapus: ")) - 1
        if 0 <= index < len(data_kegiatan):
            data_kegiatan.pop(index)
            print("Data berhasil dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")


def logout():
    print("\nKamu berhasil logout. Sampai jumpa lagi!")
    return True


def menu_ketua():
    print("Halo Ketua! Selamat datang di menu anda")
    while True:
        print("\n MENU KETUA ")
        print("1. Lihat Data")
        print("2. Logout")

        try:
            pilih = int(input("Pilih menu: "))
            if pilih == 1:
                tampilkan_kegiatan(data_kegiatan)
            elif pilih == 2:
                print("Logout dari menu Ketua...")
                logout()
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")


def menu_sekretaris():
    print("Selamat datang Sekretaris")
    while True:
        print("\n MENU SEKRETARIS ")
        print("1. Tambah data")
        print("2. Lihat data")
        print("3. Update data")
        print("4. Hapus data")
        print("5. Logout")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
            if pilih == 1:
                tambah_kegiatan()
            elif pilih == 2:
                tampilkan_kegiatan(data_kegiatan)
            elif pilih == 3:
                update_data()
            elif pilih == 4:
                hapus_data()
            elif pilih == 5:
                print("Keluar dari menu sekretaris...")
                logout()
                break
            elif pilih == 6:
                print("Keluar dari Program, Selamat tinggal...")
                exit()
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")


def menu_anggota(user_login):
    print(f"Halo {user_login}, Selamat datang! ini adalah menu yang dapat anda lihat")
    while True:
        print("\n MENU ANGGOTA ")
        print("1. Lihat Data")
        print("2. Logout")

        try:
            pilih = int(input("Pilih menu: "))
            if pilih == 1:
                tampilkan_kegiatan(data_kegiatan)
            elif pilih == 2:
                print("Logout dari menu Anggota...")
                logout()
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")


def main():
    while True:
        user_login = login()
        if user_login:
            role = pilih_role()
            if role == "Ketua":
                menu_ketua()
            elif role == "Sekretaris":
                menu_sekretaris()
            elif role == "Anggota":
                menu_anggota(user_login)
        else:
            print("Coba login lagi.\n")

main()
