# run.py

from app import init_db, SessionLocal
from app.services import KaryawanService
from sqlalchemy.orm import Session

def tampilkan_semua_karyawan(service: KaryawanService):
    """Fungsi untuk mengambil dan menampilkan data karyawan dalam format tabel."""
    print("\n--- Daftar Semua Karyawan ---")
    karyawan_list = service.lihat_semua_karyawan()
    if not karyawan_list:
        print("Belum ada data karyawan.")
        return
        
    # Header tabel
    print(f"{'ID'} | {'NAMA'} | {'NIP':<11} | {'JABATAN'}")
    print("-" * 50)
    
    # Isi tabel
    for k in karyawan_list:
        print(f"{k.id} | {k.nama} | {k.nip} | {k.jabatan}")
    print("-" * 50)


def tambah_karyawan_baru(service: KaryawanService):
    """Fungsi untuk meminta input dan menambah karyawan baru."""
    print("\n--- Tambah Karyawan Baru ---")
    try:
        nama = input("Masukkan Nama   : ")
        nip = input("Masukkan NIP    : ")
        jabatan = input("Masukkan Jabatan: ")
        
        if not nama or not nip or not jabatan:
            print("\n[ERROR] Semua field wajib diisi.")
            return

        data = {
            'nama': nama,
            'nip': nip,
            'jabatan': jabatan
        }
        karyawan_baru = service.tambah_karyawan(data)
        print(f"\n[SUKSES] Karyawan '{karyawan_baru.nama}' dengan ID {karyawan_baru.id} berhasil ditambahkan.")

    except ValueError as e:
        # Menangkap error validasi dari service (misal: NIP duplikat)
        print(f"\n[ERROR] Gagal menambahkan: {e}")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan tidak terduga: {e}")


def hapus_karyawan_by_id(service: KaryawanService):
    """Fungsi untuk menghapus karyawan berdasarkan ID."""
    print("\n--- Hapus Karyawan ---")
    try:
        karyawan_id_str = input("Masukkan ID Karyawan yang akan dihapus: ")
        karyawan_id = int(karyawan_id_str)
        
        service.hapus_karyawan(karyawan_id)
        print(f"\n[SUKSES] Karyawan dengan ID {karyawan_id} berhasil dihapus.")
        
    except ValueError as e:
        # Menangkap error jika input bukan angka atau karyawan tidak ditemukan
        print(f"\n[ERROR] Gagal menghapus: {e}")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan tidak terduga: {e}")

def main():
    """Fungsi utama untuk menjalankan aplikasi konsol."""
    # Inisialisasi database dan service
    init_db()
    db_session: Session = SessionLocal()
    karyawan_service = KaryawanService(db_session)

    while True:
        print("\n===== MENU SISTEM INFORMASI KEPEGAWAIAN =====")
        print("1. Lihat Semua Karyawan")
        print("2. Tambah Karyawan")
        print("3. Hapus Karyawan")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-4): ")

        if pilihan == '1':
            tampilkan_semua_karyawan(karyawan_service)
        elif pilihan == '2':
            tambah_karyawan_baru(karyawan_service)
        elif pilihan == '3':
            hapus_karyawan_by_id(karyawan_service)
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            db_session.close()
            break
        else:
            print("\n[ERROR] Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi utama
if __name__ == '__main__':
    main()