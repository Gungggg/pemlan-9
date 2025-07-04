# app/services.py

from datetime import date
from .models import Karyawan
from .repositories import KaryawanRepository

class KaryawanService:
    def __init__(self, session):
        self.repository = KaryawanRepository(session)

    def tambah_karyawan(self, data):
        """Logika bisnis untuk menambah karyawan baru."""
        # 1. Validasi data input
        if not all(k in data for k in ['nama', 'nip', 'jabatan']):
            raise ValueError("Data nama, nip, dan jabatan wajib diisi.")

        # 2. Aturan bisnis: NIP tidak boleh duplikat
        if self.repository.get_by_nip(data['nip']):
            raise ValueError(f"NIP '{data['nip']}' sudah terdaftar.")

        # 3. Membuat objek model
        karyawan_baru = Karyawan(
            nama=data['nama'],
            nip=data['nip'],
            jabatan=data['jabatan'],
            tanggal_masuk=date.today()
        )

        # 4. Memanggil repository untuk menyimpan ke DB
        return self.repository.add(karyawan_baru)

    def lihat_semua_karyawan(self):
        """Mengambil semua data karyawan."""
        return self.repository.get_all()

    def hapus_karyawan(self, karyawan_id):
        """Logika bisnis untuk menghapus karyawan."""
        karyawan = self.repository.get_by_id(karyawan_id)
        if not karyawan:
            raise ValueError(f"Karyawan dengan ID {karyawan_id} tidak ditemukan.")
        
        self.repository.delete(karyawan)