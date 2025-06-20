import csv
import json
import os

from osoba_class import Osoba


osoby = [] 

def wczytaj_z_json(nazwa_pliku="osoby.json"):
    global osoby
    try:
        with open(nazwa_pliku, "r") as plik:
            dane = json.load(plik)
            osoby = [Osoba.from_dict(o) for o in dane]
            print(f"\nZaladowano {len(osoby)} osob z pliku {nazwa_pliku}")
    except FileNotFoundError:
        print("Plik nie istnieje — zaczynamy z pustą lista.")
    except Exception as e:
        print(f"Blad przy wczytywaniu: {e}")

def zapisz_do_json(nazwa_pliku="osoby.json"):
    with open(nazwa_pliku, "w") as plik:
        json.dump([o.to_dict() for o in osoby], plik, indent=4)
    print(f"Zapisano {len(osoby)} osob do pliku {nazwa_pliku}")

def dodaj_osobe():
    print("\n[+] Dodaj osobe:")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    wiek = int(input("Wiek: "))
    email = input("Email: ")
    osoby.append(Osoba(imie, nazwisko, wiek, email))
    print("Osoba dodana.")

def usun_osobe():
    nazwisko = input("Podaj nazwisko do usuniecia: ")
    global osoby
    przed = len(osoby)
    osoby = [o for o in osoby if o.nazwisko.lower() != nazwisko.lower()]
    ile = przed - len(osoby)
    print(f"Usunięto {ile} osoba/osob." if ile else "[!] Nie znaleziono osoby.")

def wyswietl_osoby():
    if not osoby:
        print("Brak danych.")
    else:
        print("\n Lista osob:")
        for o in osoby:
            print(f" - {o}")


osoby = [
    Osoba("Jan","Kowalski",23,"jaski@gmail.com"),
    Osoba("Kasia","Krol",30,"kasiol@gmail.com"),
    Osoba("Piotr","Dom",35,"dotr@gmail.com"),
    Osoba("Pawel","Mily",45,"milypawel@gmail.com"),
    Osoba("Kuba","Calus",39,"kulus@gmail.com"),
]
print("Osoby1")
print(osoby)

with open("osoby.txt","w") as plik_txt:  
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


def menu():
    while True:
        print("\n========= MENU =========")
        print("1. Wyswietl osoby")
        print("2. Dodaj osobe")
        print("3. Usun osobe po nazwisku")
        print("4. Zapisz do JSON")
        print("5. Wczytaj z JSON")
        print("0. Wyjdz")
        print("========================")

        wybor = input("Wybierz opcje: ")
        if wybor == "1":
            wyswietl_osoby()
        elif wybor == "2":
            dodaj_osobe()
        elif wybor == "3":
            usun_osobe()
        elif wybor == "4":
            zapisz_do_json()
        elif wybor == "5":
            wczytaj_z_json()
        elif wybor == "0":
            print("Zakonczono.")
            break
        else:
            print("Nieprawidłowa opcja.")

