from view.mahasiswa import kabul
from view.input_form import forum as f 
t=kabul.tabel
class mahasiswa:
    def __init__(self, nama, NIM):
        self.nama = nama    
        self.NIM = NIM
        self.Nilai_Tugas = None
        self.Nilai_UTS = None
        self.Nilai_UAS = None
        self.Nilai_Akhir = None
class datamahasiswa:
    def __init__(self):
        pass
    def tambah(self):
    # method ini akan menambahkan data yang sudah diterima oleh method minta
    # ke dalam dictionary
        nama = f.namamu(self, harus_ada=False)
        self.m[nama] = f.minta(self, nama)
        print("Data berhasil ditambahkan.") 
    def ubah(self):
    # method akan mencari data dengan nama yang sesuai
    # kemudian meminta input data baru
    # input tersebut akan menggantikan data yang sudah ada
        nama = f.namamu(self, harus_ada=True)
        # method namamu dipakai untuk membedakan antara method tambah dan ubah
        # untuk konteks lihat method minta
        self.m[nama] = f.minta(self, nama) 
        print("Data berhasil diubah.") 
    def hapus(self):
    # method ini gunanya untuk hapus data dari dictionary
        nama = f.namamu(self, harus_ada=True)
        # method namamu disini untuk memastikan bahwa nama yang diinput itu ada di dictionary
        del self.m[nama]
        print("Data berhasil dihapus.")
    def lihat(self):
    # method untuk menampilkan data yang ada di dictionary
        t(self.m, title="Data Mahasiswa") 
    def cari(self):
    # akan mencari dengan nama
    # data dengan nama tersebut akan ditamplikan kepada user
        nama = f.namamu(self, harus_ada=True)
        # method namamu sama seperti yang ada di method hapus
        # untuk memastikan bahwa nama yang diinput itu ada di dictionary
        t({nama: self.m[nama]}, title=f"Data Mahasiswa dengan Nama {nama}")
    def exit(self):
        print("Program selesai.")
        exit()
