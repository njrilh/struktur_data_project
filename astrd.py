# tampungan
inp1 = []
inp2 = []
eu = False
mulG = False

inpe = int(input("Masukan ada berapa ruas(e) = "))

for i in range (inpe) :
    inp1.append(str(input(f"Ruas e{i+1} dari simpul = ")))
    inp2.append(str(input("ke simpul = ")))

totalSimpul = list(set(inp1 + inp2))
derajatGraph = len(totalSimpul) * 2
print(f"{inp1}\n{inp2}\nOrder = {len(totalSimpul)}\nSize = {inpe}\nDerajat Graph = {derajatGraph}")

# identfikasi Euler
for i in  range (len(totalSimpul)) :
    if (inp1+inp2).count(totalSimpul[i])%2 == 0 :
        eu = True
    else : break
print("Ini Euler" if eu else " Ini bukan Euler")

# identfksi multigraph
for i in range (len(inp1)-1) :
    if (inp1[i]) == (inp2[i]) or ((inp1[i] == inp1[i+1]) and (inp2[i] == inp2[i+1])) or ((inp2[i] ==inp1[i+1] and inp1[i] == inp2[i+1])) :
        mulG = True
    else: break
print("Ini Multigraph" if mulG else "Ini Simple Graph")

