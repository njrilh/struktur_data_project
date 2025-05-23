# graph asli
arrA = ["a", "b", "c", "d", "a"]
arrB = ["b", "c", "d", "a", "c"]

# graph turunan
inp1 = []
inp2 = []

edg = int(input("Ada berapa rusa dalam graph turunan ? = "))
for i in range (edg) :
    in1 = str(input(f"Ruas dari simpul = "))
    in2 = str(input("ke simpul = "))
    if len(inp1)+len(inp2) == 0 :
        inp1.append(in1)
        inp2.append(in2)
    elif inp2[i-1] == in2 :
        inp1.append(in2)
        inp2.append(in1)
    else :
        inp1.append(in1)
        inp2.append(in2)
print(f"{inp1}\n{inp2}")

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
