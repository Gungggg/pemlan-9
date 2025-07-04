# app/controllers.py

from flask import Blueprint, request, jsonify, g
from .services import KaryawanService

# Membuat Blueprint untuk mengelompokkan route terkait karyawan
karyawan_api = Blueprint('karyawan_api', __name__)

@karyawan_api.route('/karyawan', methods=['POST'])
def add_karyawan():
    data = request.get_json()
    # g.db_session didapatkan dari application context
    service = KaryawanService(g.db_session)
    
    try:
        karyawan_baru = service.tambah_karyawan(data)
        return jsonify(karyawan_baru.to_dict()), 201 # 201 Created
    except ValueError as e:
        return jsonify({'error': str(e)}), 400 # 400 Bad Request

@karyawan_api.route('/karyawan', methods=['GET'])
def get_all_karyawan():
    service = KaryawanService(g.db_session)
    karyawan_list = service.lihat_semua_karyawan()
    return jsonify([k.to_dict() for k in karyawan_list]), 200

@karyawan_api.route('/karyawan/<int:karyawan_id>', methods=['DELETE'])
def delete_karyawan(karyawan_id):
    service = KaryawanService(g.db_session)
    try:
        service.hapus_karyawan(karyawan_id)
        return jsonify({'message': f'Karyawan dengan ID {karyawan_id} berhasil dihapus.'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404 # 404 Not Found