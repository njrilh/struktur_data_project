size = int(input("Berapa simpul? = "))
nodeName = input("Masukkan nama-nama simpul (pisahkan spasi): ").split()
indexName = {}
for i in range(len(nodeName)) :
    indexName[nodeName[i]] = i 
print(nodeName)
matrix = [[0] * size for _ in range(size)]
list = [[]for _ in range (size)]
def addEdge(u, v):
    uIdx = indexName[u]
    vIdx = indexName[v]
    matrix[uIdx][vIdx] = 1
    matrix[vIdx][uIdx] = 1
    list[uIdx].append(vIdx)
    list[vIdx].append(uIdx)
def printMatrix():
    print("matriks adjc")
    print("  ", " ".join(nodeName))
    for i, row in enumerate(matrix):
        print(nodeName[i], row)
def printList():
    print("list adjc")
    for i in range(size):
        simpul = nodeName[i]
        tetangga = [nodeName[j] for j in list[i]]
        print(f"{simpul} --> {', '.join(tetangga)}")
ruas = int(input("Masukkan total berapa ruas (edge)? = "))
for _ in range(ruas):
    inp1 = input("Masukkan simpul asal (huruf): ").strip()
    inp2 = input("Masukkan simpul tujuan (huruf): ").strip()
    addEdge(inp1, inp2)
printMatrix()
printList()
