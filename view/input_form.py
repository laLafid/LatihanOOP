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