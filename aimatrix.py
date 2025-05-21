# Daftar sisi (edges) - undirected graph
edges = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")]

# Ambil semua simpul unik
nodes = sorted(set(sum(edges, ())))  # flatten & remove duplicates
node_index = {node: i for i, node in enumerate(nodes)}

# Inisialisasi matriks adjacency
adj_matrix = [[0 for _ in nodes] for _ in nodes]

# Inisialisasi matriks incidence
inc_matrix = [[0 for _ in edges] for _ in nodes]

# Bangun adjacency & incidence matrix
for idx, (u, v) in enumerate(edges):
    i, j = node_index[u], node_index[v]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1  # jika graph tak berarah
    inc_matrix[i][idx] = 1
    inc_matrix[j][idx] = 1

# Cetak matriks adjacency
print("Matriks Adjacency:")
print("   " + "  ".join(nodes))
for i, row in enumerate(adj_matrix):
    print(f"{nodes[i]}  {'  '.join(map(str, row))}")

print("\nMatriks Incidence:")
print("   " + "  ".join(f"e{j+1}" for j in range(len(edges))))
for i, row in enumerate(inc_matrix):
    print(f"{nodes[i]}  {'  '.join(map(str, row))}")
