# file contoh penggunaan flake8 -> linting
# flake8 nama_file.py

# yapf -> memformat kode
# yapf nama_file.py
#  Jika proses linting menghasilkan pesan dengan menunjukkan baris dan kode yang mengalami kesalahan, proses memformat kode akan memberikan pesan berupa kode yang telah diperbaiki. 
# Ini artinya Anda tidak perlu mengubah kode secara manual.
class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i):
        return self.i + _i

    def kurang(self, _i):
        return self.i - _i