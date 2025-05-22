# graph asli
arrA = ["a", "b", "c", "d", "a"]
arrB = ["b", "c", "d", "a", "c"]

# graph turunan
inp1 = ["a", "b", ]
inp2 = ["b", "c", ]

# tampungan
edgeAsli = []
edgeTurunan = []
is_spanning = True

# bikin jadi bolak balik
for i in range(len(arrA)):
    edgeAsli.append((arrA[i], arrB[i]))
    edgeAsli.append((arrB[i], arrA[i]))
for i in range(len(inp1)):
    edgeTurunan.append((inp1[i], inp2[i]))
    edgeTurunan.append((inp2[i], inp1[i]))

# cek spanning atau subg
if (inp2[-1], inp1[0]) in edgeAsli :
    if inp2[-1] != inp1[0] :
        is_spanning = False

if len(inp1) < 2 :
    is_spanning = True

for i in range (len(edgeTurunan)):
    if edgeTurunan[i] not in edgeAsli:
        is_spanning = False
        break

print("Ini Spaanning Tree" if is_spanning else "Ini Subgraph")
