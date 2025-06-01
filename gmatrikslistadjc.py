size = int(input("berapa simpul? = "))
simpul = input(str("masukkan nama2 simpul (pisahkan spasi): ")).split()
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
    print("matriks adjc", "\n  ", " ".join(simpul))
    for i in range(len(matrix)):
        print(simpul[i], matrix[i])
def printList():
    print("list adjc")
    for i in range(size):
        tetangga = [simpul[j] for j in list[i]]
        print(f"{simpul[i]} --> {', '.join(tetangga)}")
ruas = int(input("masukkan total berapa ruas ? = "))
for _ in range(ruas):
    inp1 = str(input("masukkan dari simpul : ")).strip()
    inp2 = input(str("ke simpul : ")).strip()
    addRuas(inp1, inp2)
printMatrix()
printList()
