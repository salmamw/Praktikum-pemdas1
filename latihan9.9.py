#Memasukkan Variabel
harga_1Km_pertama = 4500 #Harga intul 1Km pertama
harga_Km_selanjutnya = 2000 #Harga perKM selanjutnya

#Jarak diinput oleh user
jarak = float(input("Masukan jarak: "))
 
 #Menghasilkan hitung jarak
if jarak <= 1 : 
   total_sewa = harga_1Km_pertama
else:
   total_sewa = harga_1Km_pertama + (jarak-1) * harga_Km_selanjutnya
print("Total sewa angkutan:", "Rp.", total_sewa)
