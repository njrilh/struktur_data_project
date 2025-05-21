# arr simpul dan value
a = ["a", "b", "c", "d", "b"]
b = ["b", "c", "d", "a", "d"]
v = [1, 4, 2, 1, 4]

awal = str(input("Masukan simpul awal = "))
akhir = str(input("Masukan simpul akhir = "))

# tampungan
jalur = []
vJalur = []
hasil = []

# mencari semua jalur dari awal ke akhir
def cari_jalur(posisi, total, sudah_dilewati):
    if posisi == akhir:
        vJalur.append(total)
        jalur.append(sudah_dilewati)
        return

    for i in range(len(a)):
        if a[i] == posisi and b[i] not in sudah_dilewati:
            cari_jalur(b[i], total + [v[i]], sudah_dilewati + [b[i]])
        elif b[i] == posisi and a[i] not in sudah_dilewati:
            cari_jalur(a[i], total + [v[i]], sudah_dilewati + [a[i]])

# menjumlahkan seluruh value dari tiap jalur ditemukan
def jumHasil() :
     for i in range (len(vJalur)) :
         hasil.append(sum(vJalur[i]))

# eksekusi function
cari_jalur(awal, [], [awal])
jumHasil()

# ctak 
print("Hasil pencarian semua ruas = ", jalur)
print("Hasil value pencarian semua ruas = ", vJalur)
print("Semua total bobot dari", awal, "ke", akhir, "= ", hasil)
if len(hasil) > 0:
    print("Minimum Spanning Tree= ", min(hasil), "\nCritical Path = ", max(hasil))
else:
    print("Tidak ada jalur ditemukan.")