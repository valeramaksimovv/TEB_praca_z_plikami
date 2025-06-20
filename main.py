from osoba_class import Osoba
import json

osoby = []

def wczytaj_z_json(nazwa_pliku="osoby.json"):
    global osoby
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            dane = json.load(plik)
            osoby = [Osoba.from_dict(o) for o in dane]
            print(f"\nZaladowano {len(osoby)} osob z pliku {nazwa_pliku}")
    except FileNotFoundError:
        print("Plik nie istnieje — zaczynamy z pustą lista.")
    except Exception as e:
        print(f"Blad przy wczytywaniu: {e}")

def zapisz_do_json(nazwa_pliku="osoby.json"):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump([o.to_dict() for o in osoby], plik, indent=4, ensure_ascii=False)
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
    print(f"Usunieto {ile} osoba/osob." if ile else "[!] Nie znaleziono osoby.")

def wyswietl_osoby():
    if not osoby:
        print("Brak danych.")
    else:
        print("\n Lista osob:")
        for o in osoby:
            print(f" - {o}")

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

if __name__ == "__main__":
    wczytaj_z_json()
    menu()
