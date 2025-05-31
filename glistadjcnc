size = int(input("Berapa simpul? = "))
node_names = input("Masukkan nama-nama simpul (pisahkan spasi): ").split()
name_to_index = {}
for i in range(len(node_names)):
    name_to_index[node_names[i]] = i
adj_list = [[] for _ in range(size)]
def add_edge(u, v):
    u_idx = name_to_index[u]
    v_idx = name_to_index[v]
    adj_list[u_idx].append(v_idx)
    adj_list[v_idx].append(u_idx)
def print_adj_list():
    for i in range(size):
        simpul = node_names[i]
        tetangga = [node_names[j] for j in adj_list[i]]
        print(f"{simpul} --> {', '.join(tetangga)}")
ruas = int(input("Masukkan total berapa ruas (edge)? = "))
for _ in range(ruas):
    inp1 = input("Masukkan simpul asal (huruf): ").strip()
    inp2 = input("Masukkan simpul tujuan (huruf): ").strip()
    add_edge(inp1, inp2)
print(node_names, name_to_index, adj_list)
print("\nAdjacency List:")
print_adj_list()
