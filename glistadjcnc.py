size = int(input("Berapa simpul? = "))
node_names = input("Masukkan nama-nama simpul (pisahkan spasi): ").split()
name_to_index = {}
for i in range(len(node_names)) :
    name_to_index[node_names[i]] = i 
matrix = [[0] * size for _ in range(size)]
list = [[]for _ in range (size)]
def add_edge(u, v):
    u_idx = name_to_index[u]
    v_idx = name_to_index[v]
    matrix[u_idx][v_idx] = 1
    matrix[v_idx][u_idx] = 1
    list[u_idx].append(v_idx)
    list[v_idx].append(u_idx)
def print_matrix():
    print("matriks adjc")
    print("  ", " ".join(node_names))
    for i, row in enumerate(matrix):
        print(node_names[i], row)
def print_list():
    print("list adjc")
    for i in range(size):
        simpul = node_names[i]
        tetangga = [node_names[j] for j in list[i]]
        print(f"{simpul} --> {', '.join(tetangga)}")
ruas = int(input("Masukkan total berapa ruas (edge)? = "))
for _ in range(ruas):
    inp1 = input("Masukkan simpul asal (huruf): ").strip()
    inp2 = input("Masukkan simpul tujuan (huruf): ").strip()
    add_edge(inp1, inp2)
print_matrix()
print_list()
