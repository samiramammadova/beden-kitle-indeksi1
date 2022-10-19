boy=float(input("Boyunuzu qeyd edin: " ))
kilo=float(input("Kilonuzu qeyd edin: "))
indeks=kilo/(boy**2)

if indeks<=18.49:
    print(indeks,"Zeif")
elif 18.49<indeks<25:
    print(indeks,"Ideal")
else:
    print(indeks,"Obez")