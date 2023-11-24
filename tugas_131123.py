#TUGAS 1
matriks = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for data in matriks :
    for angka in data:
        print(angka)
print()
        
#TUGAS 2
buku_alamat = [["John Doe", "555-1234"],["Jane Smith", "555-5678"],["Bob Johnson", "555-7890"]]
for data in buku_alamat:
    print(data[0], "-", data[1])
print()
    
#TUGAS 3
for i in range (1, 6):
    for j in range (1, 6):
        print(i*j, end=" ")
    print()
    
#TUGAS 4
for i in range (1, 6):
    for j in range (1, i+1):
        print(i*j, end=" ")
    print()