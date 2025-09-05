import csv

print("materi 10 - file handling")
print("------------------------")
# buka file
file_path = r"C:\Users\USER\Documents\Belajar\Pertemuan_Kelima\materi-kelas\pesan.txt"

file_pesan = open(file_path, "r")

# baca isi pesan

isi_pesan = file_pesan.read()

# tampilkan output isi pesan

print(f"ISI PESAN => {isi_pesan}")

# tutup file 
file_pesan.close()
print("\n-----------------------")
print("------read csv file------")
file_path_csv = r"\Users\USER\Documents\Belajar\Pertemuan_Kelima\materi-kelas\jajan.csv"
file_pesan = open(file_path_csv, "r")
isi_jajan = file_pesan.read()
print(f"UANG JAJAN >>>> {isi_jajan}")
file_pesan.close


print("-----READ CSV FILE------")
jajan_baru = [6, "syahid",100000]
print(f"jajan baru: {jajan_baru}")
# open () -> membuka file dari file path
# # mode 'a' -> append (tambah data)
# # newline -> tambah garis baru dengan teks kosong
# with ... as -> buka file dan otomatis tutup
with open(file_path_csv, "a", newline ="") as file_jajan:
    # aktifkan mode writer csv dari file target
    writer = csv.writer(file_jajan)
    writer.writerow(jajan_baru)

    print("sukses menambahkan data jajan baru")

print("-----READ CSV FILE------")
with open(file_path_csv, "r") as file_jajan:
    reader = csv.reader(file_jajan)
    for row in reader:
        print(f"data jajan: {row}")