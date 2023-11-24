#TUGAS1
def hitung(angka1, angka2, op):
  if op == '+':
    return angka1 + angka2
  elif op == '*':
    return angka1 * angka2
  else:
    return "Operasi tidak valid"
print(hitung(2, 4, "*")) 
print(hitung(4, 5, "+"))
print(hitung(10, 5, "-")) 
print()

#TUGAS2
def perulangan(kata, jumlah):
  for I in range(jumlah):
    print(kata)

perulangan("haiii salman", 4)
perulangan("selamat datang", 2)
print()