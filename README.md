# Program Data Nilai Mahasiswa


# Cara Kerja Program Ini
1. Menampilkan menu kepada pengguna.
2. Meminta pengguna untuk memilih salah satu opsi.
3. Memanggil fungsi yang sesuai dengan pilihan pengguna.
4. Mengulang langkah 2 sampai pengguna memilih opsi keluar.

# Flowchart
![alt text](gambar/flowchrt.png)

# Struktur Program

### Modul
```ruby
from tabulate import tabulate 
# modulnya harus ada
```
Program ini menggunakan modul Tabulate untuk menampilkan tabel data kepada pengguna.

### Class dan Method
```ruby
# di folder data, file mahasiswa.py
from view.mahasiswa import kabul
from view.input_form import forum as f 
t=kabul.tabel
class mahasiswa:
    def __init__(self, nama):
        self.nama = nama    
        self.NIM = None
        self.Nilai_Tugas = None
        self.Nilai_UTS = None
        self.Nilai_UAS = None
        self.Nilai_Akhir = None
```
```ruby
# masih di folder dan file yang sama
class datamahasiswa:
    def __init__(self):
        pass
    def tambah(self):
    # method ini akan menambahkan data yang sudah diterima oleh method minta
    # ke dalam dictionary
        nama = f.namamu(self, harus_ada=False)
        self.m[nama] = f.minta(self, nama)
        print("Data berhasil ditambahkan.") 
```
```ruby               
    def ubah(self):
    # method akan mencari data dengan nama yang sesuai
    # kemudian meminta input data baru
    # input tersebut akan menggantikan data yang sudah ada
        nama = f.namamu(self, harus_ada=True)
        # method namamu dipakai untuk membedakan antara method tambah dan ubah
        # untuk konteks lihat method minta
        self.m[nama] = f.minta(self, nama) 
        print("Data berhasil diubah.") 
```
```ruby         
    def hapus(self):
    # method ini gunanya untuk hapus data dari dictionary
        nama = f.namamu(self, harus_ada=True)
        # method namamu disini untuk memastikan bahwa nama yang diinput itu ada di dictionary
        del self.m[nama]
        print("Data berhasil dihapus.")
```
```ruby  
    def lihat(self):
    # method untuk menampilkan data yang ada di dictionary
        t(self.m, title="Data Mahasiswa") 
```  
```ruby
    def cari(self):
    # akan mencari dengan nama
    # data dengan nama tersebut akan ditamplikan kepada user
        nama = f.namamu(self, harus_ada=True)
        # method namamu sama seperti yang ada di method hapus
        # untuk memastikan bahwa nama yang diinput itu ada di dictionary
        t({nama: self.m[nama]}, title=f"Data Mahasiswa dengan Nama {nama}")
```
```ruby    
    def exit(self):
        print("Program selesai.")
        exit()
```
```ruby  
# di folder view, file input_form.py
class forum:
    def __init__(self):
        pass
    def nilai(self):
    # method untuk memastikan input adalah angka
    # dan mengulangi permintaan jika input bukan angka
    # juga untuk membatasi nilai input yang diinputkan.
        while True:
            try:
                poin = float(input("Masukang Nilai: "))
                if poin < 0 or poin > 100:
                    print(f"Nilai harus berkisar dari 0 hingga 100.")
                else:
                    return poin
            except ValueError:
                print("Input harus berupa angka!!")  
```
```ruby
    def namamu(self, harus_ada=True):
    # method ini akan meminta input nama dari user
    # dan melihat apakah nama yang diinputkan tersebut ada di dictionary atau tidak
        while True:
            self.nama = input("Masukkan Nama: ")
            if harus_ada and self.nama not in self.m:
                print("nama tidak ditemukan!")
            elif not harus_ada and self.nama in self.m:
                print("nama sudah ada di database. Masukkan nama lain!")
            else:
                return self.nama  
```
```ruby
    def minta(self, nama):
    # method ini
    # gunanya untuk mendapatkan input dari user
        tugas, uts, uas = map(forum.nilai, [
                "Masukkan Nilai Tugas: ", 
                "Masukkan Nilai UTS: ", 
                "Masukkan Nilai UAS: "
                ])
        akhir = (tugas*0.3) + (uts*0.35) + (uas*0.35)
        if nama not in self.m:
            NIM = input("Masukkan NIM (e.g. 123456789): ")
            return { # akan mengembalikan/menyerahkan data ke method yang memanggil
                "Nama": nama,
                "NIM": NIM,
                "Nilai Tugas": tugas,
                "Nilai UTS": uts,
                "Nilai UAS": uas,
                "Nilai Akhir": akhir
            }
        # sekaligus melihat apakah data dengan nama yang sama ada di dictionary
        elif nama in self.m:
            return { # lihat return diatas
                "Nama": nama,
                "NIM": self.m[nama]["NIM"], # NIM dari data lama
                "Nilai Tugas": tugas,
                "Nilai UTS": uts,
                "Nilai UAS": uas,
                "Nilai Akhir": akhir
            } 
```
```ruby
# di dalam folder view, file mahasiswa.py
class kabul: 
    def __init__(self):
        pass
    def tabel(data, headers=None, title=""):
    # method ini menggunakan modul tabulate untuk mencetak table data
        if not data: 
            table = [["Tidak ada data"]]
            print(tabulate(
                table, 
                headers =["Tidak ada data"], 
                tablefmt="fancy_grid", 
                colalign=("center",)
                ))
            return
        if headers is None:
            headers = ["No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"]
        table = []
        for i, nama in enumerate(data, start=1):
            row = [
                i, 
                nama, 
                data[nama]["NIM"], 
                data[nama]["Nilai Tugas"], 
                data[nama]["Nilai UTS"], 
                data[nama]["Nilai UAS"], 
                data[nama]["Nilai Akhir"]
                ]
            table.append(row)
        print(f"{title}")
        print(tabulate(
            table, 
            headers, 
            tablefmt="fancy_grid", 
            colalign=("center",)*7
            ))
```

### Menu
```ruby
from data.mahasiswa import datamahasiswa 
a = datamahasiswa
class main:
    def __init__(self, mahadata={}): # dictionary untuk simpan data
        self.m = mahadata 

        menu = { # dictionary untuk simpan keys
            "1": a.lihat,   "l" : a.lihat, # ketika keys itu dipanggil 
            "2": a.tambah,  "t" : a.tambah, # method pada value keys akan di panggil
            "3": a.ubah,    "u" : a.ubah,
            "4": a.hapus,   "h" : a.hapus,
            "5": a.cari,    "c" : a.cari,
            "6": a.exit,    "k" : a.exit
        }
        # isinya adalah kode warna menggunakan ANSII escape
        r,h,b,m,k,u,p = "\033[0m","\033[1;32m","\033[1;34m","\033[1;31m","\033[1;33m","\033[1;35m","\033[1;37m"
        # kemudian ada perulangan yang akan menampilkan menu pilihan
        while True:
            print(
                f"{p}L{r}ihat |", 
                f"{h}T{r}ambah |", 
                f"{b}U{r}bah |", 
                f"{m}H{r}apus |", 
                f"{k}C{r}ari |", 
                f"{u}K{r}eluar"
            )
            opsi = input("Masukkan pilihan: ").lower()
            if opsi in menu:
                menu[opsi](self)
            else:
                print("pilih yang ada saja.")             
main() # ini untuk menjalankan class main
```
Program akan terus menampilkan menu kepada pengguna sampai opsi keluar di pilih. Setiap opsi akan memanggil method yang sesuai.

# Diagram Kelas
![alt text](<gambar/diagram klass.png>)

# Output Dari Program Ini
```Menambahkan Data```
![alt text](gambar/tambah.png)


```Menampilkan tabel data```
![alt text](gambar/tampilk.png)


```Mengubah data```
![alt text](gambar/ubah.png)


```Mencari```
![alt text](gambar/cari.png)
 

```Menghapus data```
![alt text](gambar/hapus.png)


```Keluar```
![alt text](gambar/kelu.png)
