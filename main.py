import csv
import json

class Osoba:
    def __init__(self, imie, nazwisko, wiek, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.email = email

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.wiek} {self.email}"

    def to_list(self):
        return [self.imie,self.nazwisko,self.wiek,self.email]

    @classmethod
    def from_list(cls,lista):
        imie, nazwisko, wiek, email = linia
        return cls(imie,nazwisko,int(wiek),email)

    def to_dict(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "wiek": self.wiek,
            "email": self.email
        }

    @classmethod
    def from_dict(cls,slownik):
        return cls(
            slownik["imie"],
            slownik["nazwisko"],
            slownik["wiek"],
            slownik["email"]
        )






osoby = [
    Osoba("Jan","Kowalski",23,"jaski@gmail.com"),
    Osoba("Kasia","Król",30,"kasiól@gmail.com"),
    Osoba("Piotr","Dom",35,"dotr@gmail.com"),
    Osoba("Paweł","Miły",45,"milypawel@gmail.com"),
    Osoba("Kuba","Całus",39,"kulus@gmail.com"),
]
print("Osoby1")
print(osoby)

with open("osoby.txt","w") as plik_txt:      # w- zapis do pliku,  a - dopisanie do pliku, r- czytanie z pliku
    plik_txt.write("imie nazwisko wiek email\n")
    for osoba in osoby:
        plik_txt.write(osoba.__repr__()+"\n")

osoby2 = []

with open("osoby.txt","r") as plik_txt2:
    next(plik_txt2)
    for linia in plik_txt2:
        imie, nazwisko, wiek, email = linia.strip().split(" ")
        osoby2.append(Osoba(imie,nazwisko,int(wiek),email))

print("Osoby2")
print(osoby2)

with open("osoby.csv","w",newline='') as plik_csv:
    writer = csv.writer(plik_csv)
    writer.writerow(["Imie","Nazwisko","Wiek","Email"])
    for osoba in osoby:
        writer.writerow(osoba.to_list())

osoby3 =[]

with open("osoby.csv","r") as plik_csv2:
    reader = csv.reader(plik_csv2)
    next(reader)
    for linia in reader:
        osoba = Osoba.from_list(linia)
        osoby3.append(osoba)

print("Osoby3")
print(osoby3)

osoby_dict = [o.to_dict() for o in osoby]
with open("osoby.json","w") as plik_json:
    json.dump(osoby_dict,plik_json,indent=4)

osoby4=[]
with open("osoby.json","r") as plik_json2:
    dane = json.load(plik_json2)
    osoby4 = [Osoba.from_dict(o) for o in dane]
print("Osoby4")
print(osoby4)


# Zadanie 1

suma_wiek = sum(osoba.wiek for osoba in osoby3)
sredni_wiek = suma_wiek / len(osoby3)
print(f"Średni wiek osób: {sredni_wiek:.2f}")

X = int(input("Podaj wiek X: "))
starsze_osoby = [osoba for osoba in osoby3 if osoba.wiek > X]
print(f"Osoby starsze niż {X} lat:")
for osoba in starsze_osoby:
    print(f"  - {osoba}")

osoby_posortowane = sorted(osoby3, key=lambda o: o.nazwisko)

with open("osoby_posortowane.csv", "w", newline='') as plik_sort:
    writer = csv.writer(plik_sort)
    writer.writerow(["Imie", "Nazwisko", "Wiek", "Email"])
    for osoba in osoby_posortowane:
        writer.writerow(osoba.to_list())

print("Zapisano osoby_posortowane.csv")

