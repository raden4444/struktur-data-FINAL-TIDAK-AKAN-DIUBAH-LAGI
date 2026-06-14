data_pasien = {}
import re

class Pasien:
    def __init__(self, id_pasien, nama, usia, keluhan, tingkat_urgensi):
        self.id_pasien = id_pasien
        self.nama = nama
        self.usia = usia
        self.keluhan = keluhan
        self.tingkat_urgensi = tingkat_urgensi
        self.rekam_medis = []

    def tampilkan_data(self):
        print("===== DATA PASIEN =====")
        print("ID      :", self.id_pasien)
        print("Nama    :", self.nama)
        print("Usia    :", self.usia)
        print("Keluhan :", self.keluhan)
        print("Urgensi :", self.tingkat_urgensi)

def tambah_pasien():
    # Mencegah ID Kosong, Duplikat, atau salah format
    while True:
        id_pasien = (input("Masukkan ID Pasien = ")).strip().upper()
        if id_pasien == "":
           print("ID pasien tidak boleh kosong")
        elif id_pasien in data_pasien:
           print("ID pasien sudah digunakan!")
        # REKREASI REGEX : Memastikan ID harus diawali huruf 'P' dan diikuti tepat 3 digit angka
        elif not re.match(r'^P\d{3}$', id_pasien):
            print("Format ID salah! Harus berupa 'P' diikuti 3 digit angka (Contoh: P001)")
        else:
           break

    while True:      
        Nama = input("Masukkan Nama = ")
        # VALIDASI NAMA: Menghapus spasi sementara untuk memastikan input hanya berisi huruf (A-Z)
        if Nama.replace(" ","").isalpha():
            break
        print ("Input tidak sesuai, Mohon masukan nama anda!")
    
    while True:
        # VALIDASI USIA: Mencegah salah input dan usia yang tidak wajar
        try:
            Usia = int(input("Masukkan Usia Pasien = "))
            if 0 < Usia < 150:
                break
            print("Usia tidak logis! mohon masukkan rentang 1 sampai 149 tahun")
        except ValueError:
            print("Usia harus berupa angka")
    
    while True:
        Keluhan = input("Masukkan Keluhan = ").strip()
        if Keluhan != "":
            break
        print ("Masukan keluhan !")
    
    while True:
        tingkat_urgensi = input("Tingkat urgensi (rendah/tinggi ) = ").strip().upper().replace(" ","")
        if tingkat_urgensi == "TINGGI" or tingkat_urgensi == "RENDAH":
            break
        else:
            print("Jawaban tidak valid!")
    
    data_pasien[id_pasien] = Pasien(
        id_pasien,
        Nama,
        Usia,
        Keluhan,
        tingkat_urgensi.capitalize()
    )

    print("Pasien berhasil ditambahkan")

def cari_pasien():

    if not data_pasien:
        print("Belum ada data pasien.")
        return

    while True:
        cari = input("Masukkan ID pasien yang dicari (ketik 0 untuk batal) = ").strip().upper().replace(" ", "")

        if cari in data_pasien:
            pasien = data_pasien[cari]
            pasien.tampilkan_data()
            break
        elif cari == "0":
            return
        else:
            print("Pasien tidak ditemukan, coba lagi.")

def hapus_pasien():
    
    id_hapus = (input("Masukkan id yang ingin dihapus : ")).strip().upper().replace(" ", "")

    if id_hapus in data_pasien:
      del data_pasien[id_hapus]
      print("Data berhasil dihapus")

    else:
        print("Pasien tidak ditemukan")

def update_pasien():
    id_update = input("Masukkan ID pasien yang ingin diubah = ").strip().upper().replace(" ", "")
    if id_update in data_pasien:
        pasien = data_pasien[id_update]
        print("===== DATA LAMA =====")
        print("Nama     :", pasien.nama)
        print("Usia     :", pasien.usia)
        print("Keluhan  :", pasien.keluhan)
        print("Tingkat Urgensi  :", pasien.tingkat_urgensi)
    
        print("===== MASUKKAN DATA BARU =====")
        
        while True:
            nama_baru = input("Masukkan Nama Baru = ")
            if nama_baru.replace(" ","").isalpha():
                break
            print ("Input tidak sesuai, Mohon masukan nama anda!")
            
        while True:
            try:
                usia_baru = int(input("Masukkan Usia Baru = "))
                if 0 < usia_baru < 150:
                    break
                print("Usia tidak logis! Masukkan rentang 1 sampai 149 tahun.")
            except ValueError:
                print("Usia harus angka")

        while True:
            keluhan_baru = input("Masukkan Keluhan Baru = ").strip()
            if keluhan_baru != "":
                break
            print("Masukkan keluhan!")

        while True:
            tingkat_urgensi_baru = input("Tingkat urgensi (rendah/tinggi )= ").strip().upper().replace(" ","")
            if tingkat_urgensi_baru == "TINGGI" or tingkat_urgensi_baru == "RENDAH":
                break
            else:
                print("Jawaban tidak valid!")

        pasien.nama = nama_baru
        pasien.usia = usia_baru
        pasien.keluhan = keluhan_baru
        pasien.tingkat_urgensi = tingkat_urgensi_baru.capitalize()

        print("Data pasien berhasil diupdate")

    else:
        print("Pasien tidak ditemukan")  
