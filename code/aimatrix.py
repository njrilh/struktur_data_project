# # Daftar sisi (edges) dari graph tak berarah
# edges = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")]

# # Ambil semua simpul (nodes) unik dari edges
# nodes = []
# for u, v in edges:
#     if u not in nodes:
#         nodes.append(u)
#     if v not in nodes:
#         nodes.append(v)

# # Urutkan node biar rapi
# nodes.sort()

# # Buat dictionary untuk menyimpan posisi index dari setiap node
# node_index = {}
# for i in range(len(nodes)):
#     node_index[nodes[i]] = i

# # Buat matriks adjacency, isinya 0 dulu
# adj_matrix = []
# for i in range(len(nodes)):
#     row = []
#     for j in range(len(nodes)):
#         row.append(0)
#     adj_matrix.append(row)

# # Buat matriks incidence, isinya 0 juga
# inc_matrix = []
# for i in range(len(nodes)):
#     row = []
#     for j in range(len(edges)):
#         row.append(0)
#     inc_matrix.append(row)

# # Isi matriks adjacency dan incidence berdasarkan edges
# for e_index in range(len(edges)):
#     u, v = edges[e_index]
#     i = node_index[u]
#     j = node_index[v]

#     # Karena graf tak berarah, tandai dua arah
#     adj_matrix[i][j] = 1
#     adj_matrix[j][i] = 1

#     # Tandai koneksi di matriks incidence
#     inc_matrix[i][e_index] = 1
#     inc_matrix[j][e_index] = 1

# # Tampilkan matriks adjacency
# print("Matriks Adjacency:")
# print("   ", end="")
# for node in nodes:
#     print(node, end="  ")
# print()
# for i in range(len(nodes)):
#     print(nodes[i], end="  ")
#     for j in range(len(nodes)):
#         print(adj_matrix[i][j], end="  ")
#     print()

# # Tampilkan matriks incidence
# print("\nMatriks Incidence:")
# print("   ", end="")
# for e in range(len(edges)):
#     print(f"e{e+1}", end=" ")
# print()
# for i in range(len(nodes)):
#     print(nodes[i], end="  ")
#     for j in range(len(edges)):
#         print(inc_matrix[i][j], end="  ")
#     print()
matrix = [[0] * 4 for _ in range(4)]
list = [[]for _ in range (4)]
print(matrix)
print(list)