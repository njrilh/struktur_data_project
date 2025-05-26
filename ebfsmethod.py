daerah = { 
 'depok': ['bekasi', 'jakarta', 'tanggerang', 'bogor'],
 'jakarta': ['depok', 'tanggerang', 'bekasi'],
 'tanggerang': ['depok', 'jakarta'],
 'bekasi': ['depok', 'bogor', 'jakarta'],
 'bogor': ['jakarta', 'bekasi', 'depok']
}
kampus = {
    'depok' : 'ubsi margonda',
    'jakarta' : 'ubsi keramat',
    'tanggerang' : 'ubsi cimone',
    'bekasi' : 'ubsi kalimalang',
    'bogor' : 'ubsi cilebut', 
}
# tampungan dan inputan
awal = str(input("Masukan asal = ")).lower()
akhir = str(input("Masukan tujuan = ")).lower()
jalur = []
# mencari semua jalur dari awal ke akhir
def cari_jalur(posisi, dilewati):
    if posisi == akhir:
        jalur.append(dilewati)
        return
    for simpul in daerah:
        if simpul == posisi:
            for tujuan in daerah[simpul]:
                if tujuan not in dilewati:
                    cari_jalur(tujuan, dilewati + [tujuan])
# eksekusi function
cari_jalur(awal, [awal])
print(f"tujuan akhir = {kampus[akhir]} \nhasil pencarian semua ruas = {jalur}, \nJalur Terpendek {min(jalur, key=len)} \njlur terpanjang {max(jalur, key=len)}")
