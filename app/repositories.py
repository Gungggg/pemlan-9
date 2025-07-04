# app/repositories.py

from .models import Karyawan
from sqlalchemy import or_ # <-- Tambahkan import 'or_'

class KaryawanRepository:
    def _init_(self, session):
        self.session = session

    # ... (metode get_by_nip, get_by_id, get_all, add, delete tetap sama) ...

    def get_by_id(self, karyawan_id):
        return self.session.query(Karyawan).filter_by(id=karyawan_id).first()
        
    def get_all(self):
        return self.session.query(Karyawan).all()

    def add(self, karyawan):
        self.session.add(karyawan)
        self.session.commit()
        self.session.refresh(karyawan)
        return karyawan

    def delete(self, karyawan):
        self.session.delete(karyawan)
        self.session.commit()

    # --- TAMBAHKAN METODE BARU DI BAWAH INI ---
    def search(self, query_term):
        """Mencari karyawan berdasarkan nama atau NIP yang cocok sebagian."""
        search_pattern = f"%{query_term}%"
        return self.session.query(Karyawan).filter(
            or_(
                Karyawan.nama.ilike(search_pattern),
                Karyawan.nip.ilike(search_pattern)
            )
        ).all()