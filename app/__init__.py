# app/__init__.py

from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from .controllers import karyawan_api

# --- Konfigurasi Database ---
DATABASE_URL = "sqlite:///simpeg.db" # Menggunakan SQLite untuk kemudahan
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Membuat tabel di database jika belum ada."""
    Base.metadata.create_all(bind=engine)

def create_app():
    app = Flask(__name__)
    
    # Mendaftarkan blueprint controller
    app.register_blueprint(karyawan_api, url_prefix='/api')
    
    # Membuat sesi database untuk setiap request
    @app.before_request
    def before_request():
        g.db_session = SessionLocal()

    # Menutup sesi database setelah request selesai
    @app.teardown_appcontext
    def teardown_db(exception=None):
        db_session = g.pop('db_session', None)
        if db_session is not None:
            db_session.close()

    return app