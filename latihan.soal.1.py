suhu = int(input("Masukkan suhu: ")) 

if suhu < 20:
    print("Suhu normal")
elif suhu >= 20 and suhu <= 25:
    print("Suhu dingin")
else:
    print("Suhu panas")


