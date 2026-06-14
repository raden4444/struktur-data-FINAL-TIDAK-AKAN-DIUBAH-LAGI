from menu_pasien import data_pasien
from collections import deque

pasien_dilayani = []

antrian_tinggi = deque()
antrian_rendah = deque()

def masuk_antrian(id_pasien):
    if id_pasien not in data_pasien:
        print("Data pasien tidak ditemukan! Silahkan daftar terlebih dahulu")
        return
    elif id_pasien in antrian_rendah or id_pasien in antrian_tinggi:
        print("Pasien sudah ada dalam antrian!")
        return
    
    urgensi = data_pasien[id_pasien].tingkat_urgensi
    if urgensi == "Tinggi":
        antrian_tinggi.append(id_pasien)
        print("Pasien masuk antrian PRIORITAS TINGGI.")
    else:
        antrian_rendah.append(id_pasien)
        print("Pasien masuk antrian REGULER.")

def lihat_antrian():  # dipanggil saat pilihan_antrian == 1
    total = len(antrian_tinggi) + len(antrian_rendah)
    print("===== JUMLAH ANTRIAN SEKARANG =====")
    print("Total:", total, "pasien")

    print("==== Prioritas TINGGI ====")
    if antrian_tinggi:
        for i, id_p in enumerate(antrian_tinggi, start=1):
            if id_p in data_pasien:
                nama = data_pasien[id_p].nama
            else:
                nama = "Data Pasien Telah Dihapus" # Proteksi jika ada bug hapus data
            print(f"{i}. {id_p} - {nama}")
    else:
        print("(Kosong)")

    print("==== Prioritas RENDAH ====")
    if antrian_rendah:
        for i, id_p in enumerate(antrian_rendah, start=1):
            if id_p in data_pasien:
                nama = data_pasien[id_p].nama
            else:
                nama = "Data Pasien Telah Dihapus" # Proteksi jika ada bug hapus data
            print(f"{i}. {id_p} - {nama}")
    else:
        print("(Kosong)")

def panggil_pasien():  # dipanggil saat pilihan_antrian == 2
    # LOGIKA PRIORITAS: Cek dan panggil pasien dari antrian TINGGI dahulu (FIFO)
    if antrian_tinggi:
        id_dipanggil = antrian_tinggi.popleft() # Mengambil pasien pertama di antrian prioritas
        label = "PRIORITAS TINGGI"
    #  Jika antrian tinggi kosong, baru panggil dari antrian RENDAH
    elif antrian_rendah:
        id_dipanggil = antrian_rendah.popleft() # Mengambil pasien pertama di antrian reguler
        label = "REGULER"
    else:
        print("Antrian kosong! Tidak ada pasien yang menunggu.")
        return

    if id_dipanggil not in data_pasien:
        print(">>> MEMANGGIL PASIEN <<<")
        print("ID      :", id_dipanggil)
        print("Nama    : (Data Pasien Telah Dihapus dari Sistem)")
        print("Keluhan : (Tidak tersedia)")
        print("Antrian :", label)
        return
        
    pasien = data_pasien[id_dipanggil]
    print(">>> MEMANGGIL PASIEN <<<")
    print("ID      :", id_dipanggil)
    print("Nama    :", pasien.nama)
    print("Keluhan :", pasien.keluhan)
    print("Antrian :", label)

    pasien_dilayani.append(id_dipanggil)
