import json
# tambahkan module json dengan import
print("Materi 12 - JSON dile handling")
print("--------READ-------")

file_path_json= r"\Users\USER\Documents\Belajar\Pertemuan_Kelima\materi-kelas\materi.json"
with open(file_path_json, "r") as file_materi:
    # json.load() ->membaca isi file json
    data_materi = json.load(file_materi)
    # akses data json dengan "key" nya
    print(f"judul berkas: {data_materi["title"]}")
    print(f"total kelas A: {data_materi["total"]}")
    print(f"status santri: {data_materi["status_santri"]}")
    print(f"status kelulusan: {data_materi["status_lulus"]}")
    # ekstrak data list dengan for loop
    for pelajaran in data_materi["pelajaran"]:
        print(f"-->{pelajaran}")
        