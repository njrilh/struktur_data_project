# Ubah Graph Asli disini
gr1 = ["a", "b", "c", "d", "e", "a"] #Dari simpul ini
gr2 = ["b", "c", "d", "e", "a", "d"] # ke simpul ini
#----------------------------------------------------
sim = set(gr1+gr2)
print("\nGraph Asli (simpul): ", sorted(sim))
ed = [f"e{i+1}" for i in range(len(gr1))]
ruasMap = {ed[i]: (gr1[i], gr2[i]) for i in range(len(ed))}
print("Graph Asli (Ruas): ", ruasMap)
gras = []
for i in range(len(gr1)):
    gras.append((gr1[i], gr2[i])), gras.append((gr2[i], gr1[i]))
print(gras)
def identWalk(simpulPath):
    isTertutup = simpulPath[0] == simpulPath[-1]
    isWalk = True
    isTrail = True
    isPath = True
    edges = []
    nodeSeen = set()
    for i in range(len(simpulPath) - 1):
        edge = (simpulPath[i], simpulPath[i + 1])
        reverse_edge = (simpulPath[i + 1], simpulPath[i])
        if edge not in gras and reverse_edge not in gras:
            isWalk = False
        if edge in edges or reverse_edge in edges:
            isTrail = False
        edges.append(edge)
        if simpulPath[i] in nodeSeen:
            isPath = False
        nodeSeen.add(simpulPath[i])
    if simpulPath[-1] in nodeSeen:
        isPath = False
    print(f"\nUrutan simpul: {simpulPath}")
    print(f"Edge yang dilalui: {edges}")
    if isWalk:
        print("Walk Tertutup" if isTertutup else "Walk Terbuka",
              "\nTrail" if isTrail else "\nBukan Trail",
              "\nPath" if isPath else "\nBukan Path")
    else:
        print("Bukan Walk!!!")
def prosesInput(user_input):
    path = user_input.lower().split()
    if all(p.startswith("e") for p in path):
        simpulPath = []
        for i, e in enumerate(path):
            if e not in ruasMap:
                print(f"Ruas {e} tidak ditemukan!")
                return
            a, b = ruasMap[e]
            if i == 0:
                simpulPath.extend([a, b])
            else:
                last = simpulPath[-1]
                if a == last:
                    simpulPath.append(b)
                elif b == last:
                    simpulPath.append(a)
                else:
                    print(f"Ruas {e} tidak tersambung dengan simpul sebelumnya ({last})!")
                    return
        identWalk(simpulPath)
    else:
        for e in path :
            if e not in sim :
                print(f"Tidak ada simpul {e}")
                return
        identWalk(path)
inp = input("Masukkan urutan simpul (a b c ...) atau ruas (e1 e2 e3 ...): ")
prosesInput(inp)
