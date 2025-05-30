size = int(input("Berapa simpul? = "))
node_names = input("Masukkan nama-nama simpul (pisahkan spasi): ").split()
name_to_index = {name: idx for idx, name in enumerate(node_names)}
matrix = [[0] * size for _ in range(size)]
def add_edge(u, v):
    u_idx = name_to_index[u]
    v_idx = name_to_index[v]
    matrix[u_idx][v_idx] = 1
    matrix[v_idx][u_idx] = 1
def print_matrix():
    print("  ", " ".join(node_names))
    for i, row in enumerate(matrix):
        print(node_names[i], row)
ruas = int(input("Masukkan total berapa ruas (edge)? = "))
for _ in range(ruas):
    inp1 = input("Masukkan simpul asal (huruf): ").strip()
    inp2 = input("Masukkan simpul tujuan (huruf): ").strip()
    add_edge(inp1, inp2)
print_matrix()
