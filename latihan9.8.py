#Memasukkan variabel
jml_karyawan_salma = int(input("Masukkan jumlah karyawan: "))
gaji_pokok_salma = float(input("Masukkan gaji pokok: "))
pajak_salma = float
tunjangan_salma = float
jml_gaji_salma = float

#Proses menghitung pajak, tunjangan, gaji, dan jumlah gaji
pajak_salma = 0.1 * gaji_pokok_salma
tunjangan_salma = 0.2 * gaji_pokok_salma
gaji_salma = gaji_pokok_salma + tunjangan_salma + pajak_salma
jml_gaji_salma = gaji_salma * jml_karyawan_salma

#Menampilkan hasil detail tunnjangan, detail pajak dan detail gaji karyawan
print("Detail tunjangan perkaryawan: ", tunjangan_salma)
print("Detail pajak karyawan:", pajak_salma)
print("Detail Gaji ", jml_karyawan_salma, "orang:", "Rp.", jml_gaji_salma)

