for i in range(1, 11):
    if i % 2 != 0:
        print("angka ganjil pertmana dalam rentang 1 sampai 10 adalah:", i)
        break


total = 0 
while True:
        bilangan = int(input("Masukkan bilangan bulat positif (atau angka negatif untuk berhenti): "))
        if bilangan < 0:
            break 
        total += bilangan 

print("Jumlah dari bilangan-bilangan yang dimasukkan adalah:", total)


angka = 0 
for i in range(1, 51):
    if i % 5 == 0:
        print(i)
        angka += 1
    if angka == 10:
        break
