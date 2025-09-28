# Mini-Project-2-DDP

Nama: Zahra Syifa Salsabila\
Kelas: B Sistem Informasi\
NIM: 2509116057\
Tugas: Mini Project 2 DDP

# Sistem Monitoring Kegiatan PMR

## FLOWCHART

![a48caba7-9245-475d-b10e-6a6c0fc2cde7](https://github.com/user-attachments/assets/f0c9cfde-7291-44db-9823-1f81d0c1524e)


Penjelasan Alur Flowchart:
1. Start\
   Ketika pengguna ingin login, Pengguna akan diperintah untuk memasukkan username dan password. Jika tidak berhasil maka pengguna diminta untuk memasukkan kembali username dan password dengan benar. Jika berhasil, maka pengguna akan masuk ke alur selanjutnya yaitu memilih role sesuai jabatannya. Misalnya jika jabatan sebagai ketua maka pengguna akan memasukkan angka 1. Jika jabatan sebagai sekretaris maka masukkan angka 2. Jika jabatan sebagai anggota maka pengguna memasukkan angka 3.
2. Jika pengguna memasukkan angka 1 atau 3 yaitu sebagai ketua atau anggota, yang akan ditampilkan dihalamannya adalah tampilan data yang sudah ditambahkan sebelumnya oleh sekretaris.
3. jika pengguna memasukkan angka 2 yaitu sebagai sekretaris, maka dihalaman pengguna bisa:
 1. Menambahkan data
    
    Jika pengguna memilih menu Tambahkan Data, akan masuk ke langkah menambahkan data kegiatan, yaitu:

   - Kegiatan

   - Lokasi

   - Waktu dan Tanggal

   Setelah data dimasukkan, sistem akan menampilkan data yang sudah ditambahkan.
 
2. Menampilkan data
   
Jika pengguna memilih menu Tampilkan Data, sistem akan menampilkan data yang sudah dimasukkan sebelumnya. Jika belum ada data yang ditambahkan sebelumnya, sistem akan menampilkan pesan "data kosong"

3. Mengupdate data
 
Jika pengguna memilih menu Update Data, sistem akan menampilkan data terlebih dahulu. Kemudian pilih nomor yang ingin diubah. Setelah itu sistem menampilkan data terbaru yang sudah diperbarui. Jika tidak dilakukan perubahan, data tetap ditampilkan seperti sebelumnya.
 
4. Menghapus data
   
Jika pengguna memilih menu Hapus Data, sistem menampilkan data terakhir terlebih dahulu. Setelah itu Pilih nomor data yang ingin dihapus. Setelah penghapusan, sistem menampilkan data terbaru. Jika tidak ada penghapusan, data tetap ditampilkan seperti sebelumnya.

5. Logout

Jika pengguna ingin kembali ke halaman utama.

6. Keluar
   Proses berakhir jika pengguna memilih menu "Keluar".

7. End

  Program telah selesai
  
## Output

![f6da0170-d84f-4557-8915-5b0351d5715e](https://github.com/user-attachments/assets/2142d5cc-600a-46f7-9a7c-36a0e81ca3bc)

Output ini berisi login pengguna "mia" sebagai ketua PMR. Pertama mia melakukan login lalu memasukkan username dan password, setelah itu dia masuk ke halaman. Di halaman mia dapat melihat tampilan data yang sudah diberikan sekretaris. Jika sudah selesai melihat data, mia bisa melakukan logout untuk kembali ke halaman utama.

![9395c1cc-a3ed-4644-9757-9bd0c57bb34a](https://github.com/user-attachments/assets/3e6823c1-9419-473d-9798-5e9e2866f8b0)

![e5bb3e8d-c9c2-41de-b326-c058b966f676](https://github.com/user-attachments/assets/feb6af8d-86f2-4360-8737-f1c572626e44)

![66f19306-1d53-4547-9e1a-78d23cb8b720](https://github.com/user-attachments/assets/be41c3f3-4f84-4d85-b1a7-1d99e60409bc)


Output ini berisi login pengguna "zahra" sebagai sekretaris PMR. Pertama zahra melakukan login lalu memasukkan username dan password, setelah itu dia masuk ke halaman. Di halaman zahra dapat menambah, menampilkan, mengupdate, menghapus data yang ingin dimasukkan ke dalam halaman. Zahra juga bisa logout jika sudah menyelesaikan data yang ingin dimasukkan.

![8bc76dfe-bbeb-466e-a415-9e0651fd882a](https://github.com/user-attachments/assets/a427bba0-bb53-4e07-bf3f-f94468973f5c)

Output ini berisi login pengguna "sasa" sebagai anggota PMR. Pertama sasa melakukan login lalu memasukkan username dan password, setelah itu dia masuk ke halaman. Di halaman sasa dapat melihat tampilan data yang sudah diberikan sekretaris. Jika sudah selesai melihat data, sasa bisa melakukan logout untuk kembali ke halaman utama.

![c4bd3c20-8d07-4029-ae53-bd5c15f9abc8](https://github.com/user-attachments/assets/f92e836a-c1bc-4167-9304-ee6beea10638)

Output ini berisi login pengguna "zulfa" dan "kiki" untuk contoh tidak berhasil atau gagal login. Pertama zulfa dan kiki melakukan login lalu memasukkan username dan password, namun password yang diberikan salah sehingga sistem meminta untuk mencoba login ulang. 
