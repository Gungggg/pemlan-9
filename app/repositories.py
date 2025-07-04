# app/repositories.py

from .models import Karyawan

class KaryawanRepository:
    def __init__(self, session):
        self.session = session

    def get_by_nip(self, nip):
        return self.session.query(Karyawan).filter_by(nip=nip).first()

    def get_by_id(self, karyawan_id):
        return self.session.query(Karyawan).filter_by(id=karyawan_id).first()
        
    def get_all(self):
        return self.session.query(Karyawan).all()

    def add(self, karyawan):
        self.session.add(karyawan)
        self.session.commit()
        self.session.refresh(karyawan) # Refresh untuk mendapatkan ID yang di-generate DB
        return karyawan

    def delete(self, karyawan):
        self.session.delete(karyawan)
        self.session.commit()