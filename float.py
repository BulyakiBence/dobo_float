# II.
# Olvassunk be billentyűzetről tizedes törteket (float), és tároljuk őket egy listában!
# A bevitel végét a 0.0 jelzi.
# Majd oldjuk meg a következő feladatokat!
# Minden feladat előtt a program írja ki a feladat sorszámát!

# 1. Volt-e 5.5-nél nagyobb szám a listában?
# 2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!
# 3. Hány darab 1 és 2 közé eső szám szerepel a listában?
# 4. Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?
# 5. Mennyi a pozitív számok összege?

tizedes_tortek_listaja = []
egykettokozotti = []
negativ = []
pozitiv = []
while True:
    tizedes_tort= float(input("Adj megy egy tizedes törtet:"))
    tizedes_tortek_listaja.append(tizedes_tort)
    valasz = (input("Szeretnél még hozzáadni? y/n"))
    if valasz == 'y':
        continue
    else:
        break

print(tizedes_tortek_listaja)

print("Első feladat")

if any(szam > 5.5 for szam in tizedes_tortek_listaja):
    print("Volt benne 5.5-nél nagyobb")

else:
    print("Nem volt 5.5-nél nagyobb")

print("2. feladat")
talalt = False
for szam in tizedes_tortek_listaja:
    if szam.is_integer and szam < 0:
        print(f"Az első negatív egész szám helye: {tizedes_tortek_listaja.index(szam) + 1}")
        talalt = True
        break
if not talalt:
    print("Nem volt benne negatív egész szám")

print("3. felafdat")
for szam in tizedes_tortek_listaja:
    if szam > 1 and szam < 2:
         egykettokozotti.append(szam)
if len(egykettokozotti) > 0:
    print(f"Egy kettő közöttiek: {len(egykettokozotti)}")

else:
    print("Nincs benne egy kettő közötti szám.")
 
 
print("4. feladat")
for szam in tizedes_tortek_listaja:
    if szam < 0:
        negativ.append(szam)
if len(negativ) > 0:
    print(f"Negatív számok között a legnagyobb: {max(negativ)}")
    print(f"Ennek helye: {tizedes_tortek_listaja.index(max(negativ)) + 1}")
else:
    print("Nincs közte negatív")

print("5. feladat")
pozitiv_szamok = 0
for szam in tizedes_tortek_listaja:
    if szam > 0:
        pozitiv_szamok += szam
if pozitiv_szamok  > 0:
    print(f"Pozitív számok összege: {pozitiv_szamok}")
else:
    print("Nem volt benne pozitív")
