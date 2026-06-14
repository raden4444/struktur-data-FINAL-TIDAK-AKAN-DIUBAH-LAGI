from menu_pasien import data_pasien, tambah_pasien, update_pasien, cari_pasien, hapus_pasien
import rekam_medis, antrian_pasien, laporan_harian

while True:
   print ("====== SISTEM MANAJEMEN KLINIK SEHAT BERSAMA ======")
   print ("[1] Menu Pasien")
   print ("[2] Menu Antrian")
   print ("[3] Laporan Harian")
   print ("[4] Batalkan tindakan terakhir (undo)")
   print ("[0] Keluar")
   print ("Pilih dengan memasukan angka (0-4)")
   print("===================================================")
   
   try:
      pilihan = int(input("Masukkan Angka = "))
   except ValueError:
      print("\nERROR: Input harus berupa angka (0-4)! Jangan memasukkan huruf atau simbol.")
      input("\nTekan Enter untuk kembali ke menu...") 
      continue 

   if pilihan == 1:
      while True:
         print("===== Menu Pasien =====")
         print("[1] Mendaftarkan Pasien baru")
         print("[2] Mengecek Data Pasien")
         print("[3] Ubah Data Pasien")
         print("[4] Hapus Data Pasien")
         print("[5] Tambah Rekam Medis")
         print("[6] Lihat Rekam Medis")
         print("[0] Kembali")
         print("Pilih angka(0-6)")
         print("=========================")
         
         try:
            pilihan_pasien = int(input("Masukkan Angka = "))
         except ValueError:
            print("\nERROR: Input harus berupa angka (0-6)! Jangan memasukkan huruf atau simbol.")
            input("\nTekan Enter untuk kembali ke menu...") 
            continue 

         if pilihan_pasien == 1:
            tambah_pasien()
         elif pilihan_pasien == 2:
            cari_pasien()
         elif pilihan_pasien == 3:
            update_pasien()
         elif pilihan_pasien == 4:
            hapus_pasien()
         elif pilihan_pasien == 5:
            rekam_medis.tambah_rekam_medis(data_pasien)
         elif pilihan_pasien == 6:
            rekam_medis.lihat_rekam_medis(data_pasien)
         elif pilihan_pasien == 0:
            break
         else:
            print("Pilihan tidak valid!")

   elif pilihan == 2:
      while True:
         print ("===== Menu Antrian =====")
         print("[1] Jumlah Antrian sekarang")
         print("[2] Panggil pasien berikutnya")
         print("[3] Tambah Antrian")
         print("[0] Kembali")

         try:
            pilihan_antrian = int(input("Masukkan Angka = "))
         except ValueError:
            print("\nERROR: Input harus berupa angka (0-3)! Jangan memasukkan huruf atau simbol.")
            input("\nTekan Enter untuk kembali ke menu...") 
            continue 
            
         if pilihan_antrian == 1:
            antrian_pasien.lihat_antrian()
         elif pilihan_antrian == 2:
            antrian_pasien.panggil_pasien()
         elif pilihan_antrian == 3:
            id_pasien = input("Masukkan ID pasien untuk antrian = ").strip().upper()
            antrian_pasien.masuk_antrian(id_pasien)
         elif pilihan_antrian == 0:
            break
         else:
            print("Pilihan tidak valid!")

         
   elif pilihan == 3:
      while True:
         print ("===== Menu Laporan Harian =====")
         print("[1] Jumlah pasien hari ini")
         print("[2] Urutan pasien")
         print("[3] Tambah Pembayaran")
         print("[4] Riwayat pembayaran")
         print("[0] Kembali")  

         try: 
            pilih_laporan = int(input("Masukkan Angka = "))
         except ValueError:
            print("Input Harus berupa angka!")
            continue

         if pilih_laporan == 1:
            laporan_harian.jumlah_pasien_hari_ini()
         elif pilih_laporan == 2:
            laporan_harian.urutan_pasien()
         elif pilih_laporan == 3:
            laporan_harian.tambah_pembayaran(data_pasien)
         elif pilih_laporan == 4:
            laporan_harian.lihat_riwayat_pembayaran()
         elif pilih_laporan == 0:
            break
         else:
            print("Pilihan tidak valid!")

   elif pilihan == 4:
      rekam_medis.undo_tindakan(data_pasien)

   elif pilihan == 0:
      print ("===== Program Selesai =====")
      break 
   else:
      print("Pilihan tidak valid!")



   
   
