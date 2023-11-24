print("perkalian")
for i in range(1, 6):
    print (i)
    for j in range(1, 4):
        print(i, "x", j, "=", int(i * j))


print("pembagian")
for i in range(1, 6):
    print (i)
    for j in range(1, 6):
        print(i, "/", j, "=", int(i / j))


print("penjumlahan")
for i in range(1, 6):
    print (i)
    for j in range(1, 6):
        print(i, "+", j, "=", int(i + j))


print("pengurangan")
for i in range(1, 6):
    print (i)
    for j in range(1, 6):
        print(i, "-", j, "=", int(i - j))

    
kumpulan_barang = [ ["meja", "kursi", "tatakan"], ["monitor", "TV", "handphone"] ]
for barang in kumpulan_barang :
    for item in barang :
        print(item, end=", ")
    print()