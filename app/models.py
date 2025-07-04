# app/models.py

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

# Base class untuk semua model
Base = declarative_base()

class Karyawan(Base):
    __tablename__ = 'karyawan'

    id = Column(Integer, primary_key=True)
    nama = Column(String(100), nullable=False)
    nip = Column(String(20), unique=True, nullable=False)
    jabatan = Column(String(50), nullable=False)
    tanggal_masuk = Column(Date, nullable=False)

    def to_dict(self):
        """Mengubah objek menjadi dictionary agar mudah di-serialize ke JSON."""
        return {
            'id': self.id,
            'nama': self.nama,
            'nip': self.nip,
            'jabatan': self.jabatan,
            'tanggal_masuk': self.tanggal_masuk.isoformat() if self.tanggal_masuk else None
        }