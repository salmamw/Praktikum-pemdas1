#Meminta input nilai a dan b dari user
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

#Proses menukar nilai a dan b 
a = a + b  #Menjumlahkan nilai a dan b
b = a - b  #Mengambil nilai dari a
a = a - b  #Mengambil nilai dari b

#Menampilkan hasil pertukaran nilai a dan b
print("Nilai a sekarang: ", a)
print("Nilai b sekarang: ", b)