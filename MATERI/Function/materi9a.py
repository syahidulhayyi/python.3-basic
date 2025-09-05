print("MATERI 9 - FUNCTION")
print("------------------")

# funtion tidak akan di eskusi jika tidak dipanggil
def say_hello(name):
    # print("hallo mr." name)
    # kasih f diawal string untuk menysipkan variable/parameter
    print(f"halo mr. {name}")
    print("baek baek ajee")
# lambda untuk menulis fungsi yang ringkas dangen 1 baris saja
# sering disebut juga fungsi anonim(tanpa nama)
# struktur [ lambda] [ paramter]
say_hello_mini = lambda name: print(f"hello mr.{name}")
# panggil fungsi fungsi nya di bawah
say_hello("azzam")
say_hello("syahid")

print("-------------------")

say_hello_mini("harun")
say_hello_mini("hanif")


# contoh penerapan lambda dengan higder-order function
# map() -- sorted()--filter

jajan_mingguan  = [ 50000, 30000, 70000, 10000, 4500, 1500]
# sorted() -> mengurutkan data
urutkan_uang = sorted(jajan_mingguan)
urutkan_uang_terbalik = sorted(jajan_mingguan, reverse= True)
print(f"urutan uang: {urutkan_uang}")
print(f"urtan uangterbalik: {urutkan_uang}")
 
# map() --> merubah data

kurangin_uang = map(lambda uang: uang - 5000, jajan_mingguan)
# list() mengubah data objek map menjadi bentuk list
list_kurangin_uang = list(kurangin_uang)
print(f"map uang berkurang: {list_kurangin_uang}")

# filter() -> menyaring / mefilter data
jajan_banyak = filter(lambda uang: uang >= 50000, jajan_mingguan)
list_jajan_banyak = list(jajan_banyak)
print(f"filter jajan diatas 30rb: {list_jajan_banyak}")

tambahkan_uang = map(lambda uang : uang + 5000, jajan_mingguan)
list_tambahkan_uang = list(tambahkan_uang)
print(f"map uang bertambah: {list_tambahkan_uang}")