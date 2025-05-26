# tampungan dan inputan
inp1 = []
inp2 = []
eu = False
mulG = False
inpe = int(input("Masukan ada berapa ruas(e) = "))
for i in range (inpe) :
    in1 = str(input(f"Ruas e{i+1} dari simpul = ")).lower()
    in2 = str(input("ke simpul = ")).lower()
    if len(inp1)+len(inp2) == 0 :
        inp1.append(in1), inp2.append(in2)
    elif inp2[i-1] == in2 :
        inp1.append(in2), inp2.append(in1)
    else :
        inp1.append(in1), inp2.append(in2)
# identifikasi derajat graph
totalSimpul = list(set(inp1 + inp2))
derajatGraph = len(totalSimpul) * 2
print(f"{inp1}\n{inp2}\nOrder = {len(totalSimpul)}\nSize = {inpe}\nDerajat Graph = {derajatGraph}")
# identfikasi Euler
for i in  range (len(totalSimpul)) :
    if (inp1+inp2).count(totalSimpul[i])%2 == 0 :
        eu = True
print("Ini Euler" if eu else " Ini bukan Euler")
# identfksi multigraph
for u, v in zip(inp1, inp2):
    if u == v:
        mulG = True
        break
for i in range (len(inp1)-1) :
    if (((inp1[i] == inp1[i+1]) and (inp2[i] == inp2[i+1])) or ((inp2[i] ==inp1[i+1] and inp1[i] == inp2[i+1]))) :
        mulG = True
        break
print("Ini Multigraph" if mulG else "Ini Simple Graph")
