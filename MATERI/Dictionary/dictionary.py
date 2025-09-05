# array
syahid_1 = ['bogor', 17, ' 10 a']



syahid = {
    "umur": 17,
    'asal': 'bogor',
    "kelas": '20 a'
}
# operasi pada dictionary

# 1. mengakses nilainya

print(syahid["umur"])

# 2. menambahkan nilai

syahid["berat_badan"] = 75
print(syahid)
# 3. mengubah nilai

syahid["berat badan"] = 61
print(syahid)

# 4. mengurangi nilai

del(syahid["berat badan"])
print(syahid)

# 5. mengecek key

print("berat badan"in syahid)

# 6. mendapatkan semua key dan valuenya

# ------LOOPING-----

#cara ngecek ada key apa aja (keys adalah sebuah nama / judul, contohnnya : "umur": 17. "umur" ini adalah keys)
print(syahid.keys())
#cara mengecek ada value apa aja(value adalah inti / isi dari judul, conthonya: "umur": 17. "17" disini adalah value)
print(syahid.values())


for key in syahid: # ()
    print(key)

print("-------------------")

for value in syahid.values(): # cara mengambil value nya saja, maka harus memakai ini: (.values())) di akhir list tsb
    print(value)

for keys, value in syahid. items():# cara mengambil  
    print(f"{key} -> {value}")

# NESTED DICTIONARY

kelas = {
    "siswa1" : {
        "nama": "syahid",
        "umur": "17",
        "asal": "bogor",
        "hobi": {
            "hobi1": "makan",
            "hobi2": "turu",
            "hobi3": "marah"

        }
    
    },
    "siswa2": {
        "nama": "juna",
        "umur": "16",
        "asal": "bekasi"
    },
    "siswa3": {
        "nama": "harun",
        "umur": "15",
        "asal": "cilengsi"

    }
}


print(kelas["siswa1"])
print(kelas["siswa2"])
print(kelas["siswa3"])