import csv

file_path =r"C:\Users\USER\Documents\Belajar\Pertemuan_Kelima\CSV\data.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    slb = csv.reader(file_baru)
    list_read = list(slb)

    print("SEMUA DATA")
    print("-" * 20)
    for baris in list_read:
        nomor = baris [0]
        nama = baris [1]
        kelas = baris [2]

        print(f"{nomor} | {nama} | {kelas}")