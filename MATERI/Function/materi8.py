print("MATERI 8A - FNCTION BASIC")
print("=========================")

# function diawali dengan keyword ' def' 

def halo_ngab ():
    print("Hallo ngab")
    print("Hallo uga ngab")

# function dengan parameter nama
def sapa_sapa (nama) :
    print("Hallo ngab", nama)
    print("apa kabar bang", nama)
    print("================")
print("cobain fungsinya:")
halo_ngab()
sapa_sapa("vino")
sapa_sapa("syahid")
sapa_sapa("juna")

#fungsi luas persegi panjang

def luas_persegi_panjang(panjang, lebar):
    print("> panjang:", panjang)
    print("> lebar", lebar)
    rumus = panjang - lebar
    print("luas persegi panjang =", rumus)


luas_persegi_panjang(10, 20)
luas_persegi_panjang(30, 50)




