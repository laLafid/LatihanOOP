from tabulate import tabulate # modulnya harus ada
class kabul:
    def __init__(self):
        pass
    def tabel(data, headers=None, title=""):
    # fungsi ini menggunakan modul tabulate untuk mencetak table data
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