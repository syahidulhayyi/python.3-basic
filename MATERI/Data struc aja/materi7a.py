print("MATERI 7 - PYTHON DATA STRUCTURES")
print("------------------------")
# set -> {} -> tidak berurutan, tidak bisa diubah, tidak boleh duplikat
#game_azka={"valorant", "pubg", "free fire"}
#game_azka.add("mobile legend")

#print("Game Azka:", game_azka)


#game_zaky={"pubg", "free fire", "call of duty"}
#game_zaky.add("valorant")
#game_zaky.remove("call of duty") # menghapus item
#print("Game Zaky:", game_zaky)

#game_gabungan = game_azka or game_zaky #(bisa pakai tanda | atau or)
#print("daftar game gabungan:", game_gabungan)

# for (loop) untuk mengeluarkan isi item set

#for i in game_gabungan: # bisa memaakai fo / i 
   # print("-->",i)
  #  print("--> tranfer data game ",i,"ke server")


# Distionary (dict) -> {key:value} / {kunci:isi}
# -> berurutan, bisa diubah, boleh duplikat

kamus_anime = {
    'blue_lock': 'isagi',
    'one_piece': 'luffy',
    'spy_x_family': 'anya',
    'black_clover': 'asta ', 

"waifu":{ 
    'maou gakuin no futei': 'sahsa',
    'hataroku maou sama': 'emiya',
    'naruto': 'tsunade',}
}

print("kamus anime:", kamus_anime)
print("MC black clover:", kamus_anime, ["black clover"])
print("waifu naruto:", kamus_anime["waifu"]["naruto"])

# mengubah item dari dictionary
kamus_anime["naruto"] = "shikamaru"
print("MC naruto", kamus_anime["naruto"])

# mengubah item dari dictionary
kamus_anime["demon slayer"] = 'tanjiro'
print("MC demon slayer", kamus_anime["demon slayer"])

# hapus item dari dictionary
del(kamus_anime["one_piece"])
print("kAMUS ANIME TERBARU:", kamus_anime)