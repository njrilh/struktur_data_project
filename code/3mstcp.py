# Ubah aja Graphnya Disini
a = ["a", "a", "a", "b", "b", "c", "d", "d", "e", "f"] # Dari simpul ini
b = ["b", "c", "d", "c", "e", "d", "e", "f", "f", "a"] # Ke simpul ini
v = [2, 3, 6, 1, 4, 2, 1, 5, 4, 3 ] # valuenya 
#-------------------------------------------------
awal = str(input("Masukan simpul awal = ")).lower()
akhir = str(input("Masukan simpul akhir = ")).lower()
jalur = []
vJalur = []
hasil = []
def cari_jalur(posisi, total, dilewati):
    if posisi == akhir:
        vJalur.append(total), jalur.append(dilewati)
        return
    for i in range(len(a)):
        if a[i] == posisi and b[i] not in dilewati:
            cari_jalur(b[i], total + [v[i]], dilewati + [b[i]])
        elif b[i] == posisi and a[i] not in dilewati:
            cari_jalur(a[i], total + [v[i]], dilewati + [a[i]])
def jumHasil() :
     for i in range (len(vJalur)) :
         hasil.append(sum(vJalur[i]))
cari_jalur(awal, [], [awal])
jumHasil()
minj = hasil.index(min(hasil))
maxj = hasil.index(max(hasil))
print(minj, maxj)
print(f"Hasil pencarian semua ruas = {jalur} \nHasil value pencarian semua ruas = {vJalur}",
      f"\nSemua total bobot dari {awal} ke {akhir} = {hasil}")
print(f"Minimum Spanning Tree = {min(hasil)} {jalur[minj]} {vJalur[minj]}",
      f"\nCritical Path = {max(hasil)} {jalur[maxj]} {vJalur[maxj]}" if len(hasil) > 0 else "Tidak ada jalur ditemukan.")
