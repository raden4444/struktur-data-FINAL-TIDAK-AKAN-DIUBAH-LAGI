from antrian_pasien import pasien_dilayani
from datetime import datetime

riwayat_pembayaran = []

def jumlah_pasien_hari_ini():
    print(" ====== LAPORAN HARIAN ====== ")
    print("Jumlah pasien yang dilayani hari ini : ", len(pasien_dilayani))

def tambah_pembayaran(data_pasien):
    id_pasien = input("Masukkan ID pasien = ").strip().upper()

    if id_pasien not in data_pasien:
        print("Pasien tidak ditemukan!")
        return

    while True:
     try:
        total = int(input("Masukkan total pembayaran = "))
        break
     except ValueError:
        print("Input tidak valid !")
        continue

    tanggal = datetime.now().strftime("%d-%m-%Y")
    transaksi = {
        "tanggal": tanggal, 
        "id_pasien": id_pasien,
        "nama": data_pasien[id_pasien].nama,
        "total": total 
    }

    riwayat_pembayaran.append(transaksi)

    print("Pembayaran berhasil dicatat!")

def lihat_riwayat_pembayaran():
    if not riwayat_pembayaran:
        print("Belum ada transaksi pembayaran!")
        return

    print("====== RIWAYAT PEMBAYARAN ======")

    for i, transaksi in enumerate(riwayat_pembayaran, start=1):
        print(f"\nTransaksi {i}")
        print("Tanggal :", transaksi["tanggal"])
        print("ID      :", transaksi["id_pasien"])
        print("Nama    :", transaksi["nama"])
        print("Total   : Rp", transaksi["total"])