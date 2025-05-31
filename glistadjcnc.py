size = int(input("Berapa simpul? = "))
simpul = input("Masukkan nama-nama simpul (pisahkan spasi): ").split()
simpulIdx = {}
for i in range(len(simpul)) :
    simpulIdx[simpul[i]] = i 
matrix = [[0] * size for _ in range(size)]
list = [[]for _ in range (size)]
def addRuas(u, v):
    uIdx = simpulIdx[u]
    vIdx = simpulIdx[v]
    matrix[uIdx][vIdx] = 1
    matrix[vIdx][uIdx] = 1
    list[uIdx].append(vIdx)
    list[vIdx].append(uIdx)
def printMatrix():
    print("matriks adjc")
    print("  ", " ".join(simpul))
    for i, row in enumerate(matrix):
        print(simpul[i], row)
def printList():
    print("list adjc")
    for i in range(size):
        smpl = simpul[i]
        tetangga = [simpul[j] for j in list[i]]
        print(f"{smpl} --> {', '.join(tetangga)}")
ruas = int(input("Masukkan total berapa ruas (edge)? = "))
for _ in range(ruas):
    inp1 = input("Masukkan simpul asal (huruf): ").strip()
    inp2 = input("Masukkan simpul tujuan (huruf): ").strip()
    addRuas(inp1, inp2)
printMatrix()
printList()
