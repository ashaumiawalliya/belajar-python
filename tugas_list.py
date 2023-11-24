print("Selamat Datang di Dufan")
nama = input("masukan namamu: ")
umur = input("masukan umurmu: ")
print("Halo selamat datang", nama, "Di Dufan")

print("daftar wahana")
daftar_wahana = ["Biang lala Rp.13.000", "Istana Boneka Rp.15.000", "Halilintar Rp.20.000", "Rumah kaca Rp.15.000"]

angka = 1
for wahana in daftar_wahana :
    print(str(angka)+". "+wahana)
    angka = angka + 1
wahana = input("Pilih nomor wahana: ")
if wahana == "1":
    print("pilihan wahana no 1 adalah biang lala")
if wahana == "2" :
    print("Pilihan wahana no 2 adalah istana boneka")
if wahana == "3" :
    print("Pilihan wahana no 3 adalah halilintar")
if wahana == "4" :
    print("Pilihan wahana no 4 adalah rumah kaca")

if int (umur) >= 18:
    print("anda mendapat pajak sebesar Rp.2.000")
    if wahana == "1":
            print("tiket Rp.13.000 + pajak Rp.2.000 = Rp.15.000")
            print("anda harus bayar sebesar Rp.15.000")
    if wahana == "2":
            print("tiket Rp.15.000 + pajak Rp.2.000 = Rp.17.000")
            print("anda harus bayar sebesar Rp.17.000")
    if wahana == "3":
            print("tiket Rp.20.000 + pajak Rp.2.000 = Rp.22.000")
            print("anda harus bayar sebesar Rp.22.000")
    if wahana == "4":
            print("tiket Rp.15.000 + pajak Rp.2.000 = Rp.17.000")
            print("anda harus bayar sebesar Rp.17.000")
elif int(umur) < 18:
    print("Anda belum mencukupi umur untuk naik wahana")