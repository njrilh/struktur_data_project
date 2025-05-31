# menyimpan daerah asal
graph1 = { 
 'depok': ['bekasi', 'jakarta', 'tanggerang', 'bogor'],
 'jakarta': ['depok', 'tanggerang', 'bekasi'],
 'tanggerang': ['depok', 'jakarta'],
 'bekasi': ['depok', 'bogor', 'jakarta'],
 'bogor': ['jakarta', 'bekasi', 'depok']
}
# menyimpan daerah tujuan
graph2 = {
    'depok' : ['ubsi margonda'],
    'jakarta' : ['ubsi keramat'],
    'tanggerang' : ['ubsi cimone'],
    'bekasi' : ['ubsi kalimalang'],
    'bogor' : ['ubsi cilebut'], 
}
print()
# inputan titik awal dan tujuan
awal = input('Masukkan titik awal   : ').lower()
tujuan = input('Masukkan titik tujuan : ').lower()
# invalid input
if awal not in graph1 or tujuan not in graph2:
    print("Titik awal atau titik tujuan tidak valid.")
    print()
    print('================= {Rute Yang Dilewati Untuk Menuju Kampus} ===================')
    print(f'Titik Awal           : {awal}')
    print(f'Titik Tujuan(Kampus) : {tujuan}')
    print("Total kemungkinan jalur yang bisa dilewati : 0 jalur ")
    print("Jalur yang ditemukan : Tidak Ada")
    print("Rute tercepat : Tidak ada")
    print("Rute terlama  : Tidak ada")
    print('==============================================================================')
    print()
# valid input    
else:
    rute_tercepat = []
    rute_terlama = []
    jalur = [[awal]]
    jumlah_tercepat = float('inf')
    jumlah_terlama = 0
    semua_jalur = []
    while jalur:
        jalur_aktif = jalur.pop(0)
        kota_terakhir = jalur_aktif[-1]
        if kota_terakhir == tujuan:
            jumlah_kota = len(jalur_aktif)
            semua_jalur.append(jalur_aktif)
            if jumlah_kota < jumlah_tercepat:
                jumlah_tercepat = jumlah_kota
                rute_tercepat = jalur_aktif
            if jumlah_kota > jumlah_terlama:
                jumlah_terlama = jumlah_kota
                rute_terlama = jalur_aktif
        for kota_sekitar in graph1.get(kota_terakhir, []):
            if kota_sekitar not in jalur_aktif:
                jalur.append(jalur_aktif + [kota_sekitar])
    print()
    print('================= {Rute Yang Dilewati Untuk Menuju Kampus} ===================')
    print(f'Titik Awal           : {awal}')
    print('Titik Tujuan(Kampus) :',graph2[tujuan][0])
    print("Total kemungkinan jalur yang bisa dilewati : " + str(len(semua_jalur)) + " jalur ")
    print("Jalur yang ditemukan :", semua_jalur)
    print("Rute tercepat :", " -> ".join(rute_tercepat) if rute_tercepat else "Tidak ada")
    print("Rute terlama  :", " -> ".join(rute_terlama) if rute_terlama else "Tidak ada")
    print('==============================================================================')
    print()
