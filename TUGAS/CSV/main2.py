import csv

file_path =r"C:\Users\USER\Documents\Belajar\Pertemuan_Kelima\CSV\keuangan.csv"

with open(file_path, "r") as file_lama:
    next(file_lama)
    SH = csv.reader(file_lama)
    list_data = list(SH)

    print("tanggal | keterangan | kategori | jumlah")
    print("-" * 40)
    for baris in list_data:
        tanggal = baris [0]
        keterangan = baris [1]
        kategori = baris [2]
        jumlah = baris [3]

        print(f"{tanggal} | {keterangan} | {kategori} | {jumlah}")

# TAMBAH DATA
with open(file_pith, "a", newline="") as file_baru:
    write = csv.writer(file_baru)
    write.writerow({"1," "SYAHID", "10"})