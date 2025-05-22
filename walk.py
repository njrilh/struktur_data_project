# graph asli
arrA = ["a", "b", "c", "d",]
arrB = ["b", "c", "d", "a",]

# tampungan
inp1 = []
inp2 = []
edges = []
trailDilewati = []
pathDilewati = []
isWalk = True
isTrail = True
isPath =True

# input ruas simpul
for i in range(len(arrA)) :
    in1 = str(input(f"Ruas e{i+1} dari simpul = "))
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

# bikin list bolak balik
for i in range(len(arrA)) :
    edges.append((arrA[i], arrB[i]))
    edges.append((arrB[i], arrA[i]))
print(edges)

# identifikaasi walk?
for i in range(len(inp1)-1) :
    if (inp1[i], inp2[i]) not in edges :
        isWalk = False
        break
    elif inp2[i] != inp1[i+1] :
        isWalk = False
        break

# eksekusi walk
if isWalk :
    # identifikassi jenis walk 
    if inp1[0] == inp2[-1] :
        isPath = False
        print("Ini adalah WALK Tertutup")
    else :
        print("Ini adalah Walk Terbuka")

    # identifkasi trail?
    for i in range (len(inp1)) :
        if (inp1[i], inp2[i]) not in trailDilewati :
            trailDilewati.append((inp1[i], inp2[i]))
            trailDilewati.append((inp2[i], inp1[i]))
        else :
            isTrail = False
            break
    
    # eksekusi trail
    if isTrail :
            # identifikasi tath?
            for i in range (len(inp1)) :
                if inp1[i] not in pathDilewati :
                    pathDilewati.append(inp1[i])
                else :
                    isPath = False

            # eksekusi path
            if isPath :
                print("ini adalah trail dan path")
            else :
                print("ini adalah trail bukan path")

else:
    print("Ini BUKAN walk (tidak semua simpul saling terhubung)")
