# import materi7

# materi7.sapa_nama("syahid", 17) 

import MATERI.Function.rangking as rangking
import MATERI.Function.emoji as emoji

nilai = [75, 90, 60, 88, 100, 55]
nilai_urut = rangking.urutkan_nilai(nilai)
print(f"urutan nilai santri : {nilai_urut}")

nilai_tertinggi = rangking.nilai_tertinggi(nilai)
print(f"nilai tertinggi santri : {nilai_tertinggi}") 

nilai_terendah = rangking.nilai_terendah(nilai)
print(f"nilai terendah santri : {nilai_terendah}")


mood = ["senang", "kangen", "turu ieu", "apaan sih"]
print (emoji.novert_mood(mood))