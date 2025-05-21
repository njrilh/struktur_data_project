# graph asli
arrA = ["a", "b", "c", "d", "a"]
arrB = ["b", "c", "d", "a", "c"]

# graph turunan
inp1 = ["a", "b", "a"]
inp2 = ["b", "c", "c"]

# tampungan
edgeAsli = []
edgeTurunan = []

# bikin jadi bolak balik
for i in range(len(arrA)):
    edgeAsli.append((arrA[i], arrB[i]))
    edgeAsli.append((arrB[i], arrA[i]))
for i in range(len(inp1)):
    edgeTurunan.append((inp1[i], inp2[i]))
    edgeTurunan.append((inp2[i], inp1[i]))

# Cek apakah turunan adalah subgraph (semua edge-nya ada di graph asli)
is_subgraph = True
for i in range (len(edgeTurunan)):
    if edgeTurunan[i] not in edgeAsli:
        is_subgraph = False
        break

# Cek simpul dari graf asli dan graf turunan
simpulAsli = set(arrA + arrB)
simpulTurunan = set(inp1 + inp2)

is_spanning = False
if is_subgraph and simpulTurunan == simpulAsli:
    if len(edgeTurunan) // 2 == len(simpulTurunan) - 1:  # spanning tree: |E| = |V| - 1
        is_spanning = True

print("Ini Spaanning Tree" if is_spanning else "Ini Subgraph" if is_subgraph else "Ini bukan spanning dan bukan sub")
