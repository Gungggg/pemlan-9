# run.py

from app import init_db, SessionLocal
from app.services import KaryawanService
from sqlalchemy.orm import Session

def tampilkan_karyawan(karyawan_list):
    """Fungsi generik untuk menampilkan daftar karyawan dalam format tabel."""
    if not karyawan_list:
        print("Data karyawan tidak ditemukan.")
        return
        
    print(f"\n{'ID'} | {'NAMA'} | {'NIP':<11} | {'JABATAN'}")
    print("-" * 50)
    
    for k in karyawan_list:
        print(f"{k.id} | {k.nama} | {k.nip} | {k.jabatan}")
    print("-" * 50)

def tampilkan_semua_karyawan(service: KaryawanService):
    print("\n--- Daftar Semua Karyawan ---")
    karyawan_list = service.lihat_semua_karyawan()
    tampilkan_karyawan(karyawan_list)

def tambah_karyawan_baru(service: KaryawanService):
    print("\n--- Tambah Karyawan Baru ---")
    try:
        nama = input("Masukkan Nama   : ")
        nip = input("Masukkan NIP    : ")
        jabatan = input("Masukkan Jabatan: ")
        
        if not nama or not nip or not jabatan:
            print("\n[ERROR] Semua field wajib diisi.")
            return

        data = {'nama': nama, 'nip': nip, 'jabatan': jabatan}
        karyawan_baru = service.tambah_karyawan(data)
        print(f"\n[SUKSES] Karyawan '{karyawan_baru.nama}' dengan ID {karyawan_baru.id} berhasil ditambahkan.")

    except ValueError as e:
        print(f"\n[ERROR] Gagal menambahkan: {e}")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan tidak terduga: {e}")

def hapus_karyawan_by_id(service: KaryawanService):
    print("\n--- Hapus Karyawan ---")
    try:
        karyawan_id_str = input("Masukkan ID Karyawan yang akan dihapus: ")
        karyawan_id = int(karyawan_id_str)
        
        service.hapus_karyawan(karyawan_id)
        print(f"\n[SUKSES] Karyawan dengan ID {karyawan_id} berhasil dihapus.")
        
    except ValueError as e:
        print(f"\n[ERROR] Gagal menghapus: {e}")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan tidak terduga: {e}")

# --- FUNGSI BARU UNTUK PENCARIAN ---
def cari_karyawan(service: KaryawanService):
    """Fungsi untuk mencari karyawan berdasarkan input pengguna."""
    print("\n--- Cari Karyawan ---")
    query = input("Masukkan Nama atau NIP untuk mencari: ")
    try:
        hasil_pencarian = service.cari_karyawan_service(query)
        tampilkan_karyawan(hasil_pencarian)
    except ValueError as e:
        print(f"\n[ERROR] {e}")

def main():
    init_db()
    db_session: Session = SessionLocal()
    karyawan_service = KaryawanService(db_session)

    while True:
        # --- MENU DIPERBARUI ---
        print("\n===== MENU SISTEM INFORMASI KEPEGAWAIAN =====")
        print("1. Lihat Semua Karyawan")
        print("2. Tambah Karyawan")
        print("3. Hapus Karyawan")
        print("4. Cari Karyawan")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == '1':
            tampilkan_semua_karyawan(karyawan_service)
        elif pilihan == '2':
            tambah_karyawan_baru(karyawan_service)
        elif pilihan == '3':
            hapus_karyawan_by_id(karyawan_service)
        elif pilihan == '4':
            cari_karyawan(karyawan_service) # Memanggil fungsi cari
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            db_session.close()
            break
        else:
            print("\n[ERROR] Pilihan tidak valid. Silakan coba lagi.")

if _name_ == '_main_':
    main()