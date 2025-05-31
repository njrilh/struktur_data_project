size = int(input("berapa simpul? = "))
simpul = input("masukkan nama2 simpul (pisahkan spasi): ").split()
simpulIdx = {}
for i in range(len(simpul)) :
    simpulIdx[simpul[i]] = i 
print(simpul)
matrix = []
for i in range (size) :
    row = [0] * size
    matrix.append(row)
list = []
for i in range (size) :
    list.append([])
def addRuas(u, v):
    uIdx = simpulIdx[u]
    vIdx = simpulIdx[v]
    matrix[uIdx][vIdx] = 1
    matrix[vIdx][uIdx] = 1
    list[uIdx].append(vIdx)
    list[vIdx].append(uIdx)
    print(f'{matrix}\n{list}')
def printMatrix():
    print("matriks adjc", "\n  ", " ".join(simpul))
    for i, row in enumerate(matrix):
        print(simpul[i], row)
def printList():
    print("list adjc")
    for i in range(size):
        smpl = simpul[i]
        tetangga = [simpul[j] for j in list[i]]
        print(f"{smpl} --> {', '.join(tetangga)}")
ruas = int(input("masukkan total berapa ruas ? = "))
for _ in range(ruas):
    inp1 = input("masukkan dari simpul : ").strip()
    inp2 = input("masukkan ke simpul : ").strip()
    addRuas(inp1, inp2)
printMatrix()
printList()
