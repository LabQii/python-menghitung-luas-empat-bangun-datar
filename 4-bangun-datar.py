def persegi(panjang,lebar):
    luaspersegi=panjang*lebar
    return luaspersegi
def jargen(alas,tinggi):
    luasjargen=alas*tinggi
    return luasjargen
def segitiga(alas,tinggi):
    luassegitiga=1/2 * alas * tinggi
    return luassegitiga
def lingkaran(jarijari):
    luaslingkaran=22/7 * jarijari**2
    return luaslingkaran

print("\n============== MUHAMMAD IQBAL FIRMANSYAH/210441100084 ================")
print("================           INI PROGRAM SAYAAA!       ====================")
print("======= SILAHKAN PILIH, MAU MENGHITUNG BANGUN DATAR YANG MANA? ======= \n")
print("a. Persegi")
print("b. Jajargenjang")
print("c. Segitiga")
print("d. Lingkaran")

select = "y"
while select == "y" :
    pilih=str(input("\nPILIH SESUAI HURUF YANG AKAN ANDA PILIH : "))

    if pilih=="a":
        p = int(input("Masukkan panjang : "))
        l = int(input("Masukkan Lebar : "))
        print("Luas Persegi panjang dengan panjang ",p,"cm ","dan lebar ",l,"adalah => ",persegi(p,l)," cm")
        print("\n======================== TERIMAKASIH ==================================")
        print("================= SUDAH MENJALANKAN PROGRAM SAYA ======================")
    elif pilih=="b":
        a = int(input("Masukkan Alas : "))
        t = int(input("Masukkan Tinggi : "))
        print("Luas Jajargenjang dengan alas ",a,"cm ","dan tinggi ",t,"adalah => ",jargen(a,t)," cm")
        print("\n======================== TERIMAKASIH ==================================")
        print("================= SUDAH MENJALANKAN PROGRAM SAYA ======================")
    elif pilih=="c":
        al = int(input("Masukkan Alas : "))
        tg = int(input("Masukkan Tinggi : "))
        print("Luas Segitiga dengan alas ", al, "cm ", "dan tinggi ", tg, "adalah => ", segitiga(al,tg), " cm")
        print("\n======================== TERIMAKASIH ==================================")
        print("================= SUDAH MENJALANKAN PROGRAM SAYA ======================")
    elif pilih=="d" :
        r = int(input("Masukkan Jari-jari Lingkarannya : "))
        print("Luas Lingkaran dengan jari-jari ",r,"adalah : ",lingkaran(r), " cm")
        print("\n======================== TERIMAKASIH ==================================")
        print("================= SUDAH MENJALANKAN PROGRAM SAYA ======================")
    else :
        print("Maaf anda salah menginputkan!!")

    select = input("\nKAMU INGIN MENGHITUNG LAGI ? (y/t) : ")
    if select=="y":
        continue
    elif select=="t":
        print("TERIMAKASIH SUDAH MENCOBA, SEMANGAT MAHASISWA !!! ")
        break
    else :
        print("Maaf anda salah menginputkan!!")