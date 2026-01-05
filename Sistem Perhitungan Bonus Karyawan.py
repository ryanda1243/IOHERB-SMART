print("==== Sistem Perhitungan Bonus Karyawan====")
keuntungan=["15%","10%","5%"]
karyawan=int(input("Masukkan Jumlah Karyawan:"))
laba=int(input("\nMasukkan Laba yang didapatkan:"))
if laba>2000000:
    print("Selamat Anda mendapatkan bonus sebesar",keuntungan[0])
elif laba>=1000000:
    print("Selamat anda mendapatkan bonus sebesar",keuntungan[1])
elif laba>=500000:
    print("Selamat anda mendapatkan bonus sebesar",keuntungan[2])
elif laba<500000:
    print("Selamat anda mendapatkan bonus sebesar",keuntungan[2])
else:
    print("kode error")
