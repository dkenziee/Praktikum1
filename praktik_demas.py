#Nama : Moammar Demas Kenzie

print("Hitung luas ruangan")
panjang = int(input("Masukkan Panjang Ruangan :"))
lebar = int(input("masukkan Lebar Ruangan : "))
satuan = str(input("Masukkan Satuan (Meter/Inci):"))
hasil = panjang * lebar
if satuan == "Meter" :
    print("Luas ruangan dengan panjang", panjang,  "dan lebar", lebar ,"adalah" , hasil , satuan)
elif satuan == "Inci" :
    print("Luas ruangan dengan panjang", panjang, "dan lebar", lebar, "adalah", hasil, satuan)
else:
    print("Input salah")
