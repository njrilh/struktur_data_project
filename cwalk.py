# graph asli
arrA = ["a", "b", "c", "d",]
arrB = ["b", "c", "d", "a",]
# tampungan dan inputan
inp1 =[] 
inp2 =[]
edges = []
trailDilewati = []
pathDilewati = []
isWalk = True
isTrail = True
isPath =True
e = int(input("masukan berapa ruas graph turunan = "))
for i in range (e) :
    in1 = str(input(f"Ruas e{i+1} dari simpul = ")).lower()
    in2 = str(input("ke simpul = ")).lower()
    if len(inp1)+len(inp2) == 0 :
        inp1.append(in1), inp2.append(in2)
    elif inp2[i-1] == in2 :
        inp1.append(in2), inp2.append(in1)
    else :
        inp1.append(in1), inp2.append(in2)
print(f"{inp1}\n{inp2}")
# bikin list bolak balik
for i in range(len(arrA)) :
    edges.append((arrA[i], arrB[i])), edges.append((arrB[i], arrA[i]))
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
                elif inp1[0] == inp2[-1] :
                    isPath = False
                else :
                    isPath = False
            print("ini adalah trail dan path" if isPath else "ini adalah trail bukan path")
    else :
        print("ini bukan trail maupun path")
else:
    print("Ini bukan walk (tidak semua simpul saling terhubung)")
