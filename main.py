import json
import csv
from datetime import datetime
from osoba_class import Osoba


osoby = []

# json operations
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

# csv reade
def wczytaj_z_csv(nazwa_pliku="osoby.csv"):
    global osoby
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            osoby = [Osoba.from_list(row) for row in reader]
        print(f"Wczytano {len(osoby)} osob z pliku {nazwa_pliku}")
    except FileNotFoundError:
        print("Plik CSV nie istnieje.")
    except Exception as e:
        print(f"Bląd przy wczytywaniu CSV: {e}")

# csv writer
def zapisz_do_csv(nazwa_pliku="osoby.csv"):
    with open(nazwa_pliku, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Imie", "Nazwisko", "Wiek", "Email"])
        for osoba in osoby:
            writer.writerow(osoba.to_list())
    print(f"Zapisano {len(osoby)} osob do pliku {nazwa_pliku}")

# txt writer
def zapisz_do_txt(nazwa_pliku="osoby.txt"):
    with open(nazwa_pliku, "w", encoding="utf-8") as f:
        for o in osoby:
            f.write(f"{o.imie} {o.nazwisko} {o.wiek} {o.email}\n")
    print(f"Zapisano {len(osoby)} osob do pliku {nazwa_pliku}")

# add person
def dodaj_osobe():
    print("\n[+] Dodaj osobe:")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    wiek = int(input("Wiek: "))
    email = input("Email: ")
    osoby.append(Osoba(imie, nazwisko, wiek, email))
    print("Osoba dodana.")
    zapisz_log(f"Dodano osobe: {imie} {nazwisko}, {wiek} lat, {email}")

# rm person
def usun_osobe():
    nazwisko = input("Podaj nazwisko do usuniecia: ")
    global osoby
    przed = len(osoby)
    osoby = [o for o in osoby if o.nazwisko.lower() != nazwisko.lower()]
    ile = przed - len(osoby)
    print(f"Usunieto {ile} osoba/osob." if ile else "[!] Nie znaleziono osoby.")
    zapisz_log(f"Usunieto osoby z nazwiskiem: {nazwisko} ({ile} szt.)")

def wyswietl_osoby():
    if not osoby:
        print(" !X! Brak danych.")
    else:
        print("\n Lista osob:")
        for o in osoby:
            print(f" - {o}")

# edit person
def edytuj_osobe():
    nazwisko = input("Podaj nazwisko osoby do edycji: ").lower()
    znalezione = [o for o in osoby if o.nazwisko.lower() == nazwisko]

    if not znalezione:
        print("[!] Nie znaleziono osoby.")
        return

    osoba = znalezione[0]
    print(f"Znaleziono: {osoba}")

    nowe_imie = input(f"Nowe imię (ENTER = {osoba.imie}): ") or osoba.imie
    nowe_nazwisko = input(f"Nowe nazwisko (ENTER = {osoba.nazwisko}): ") or osoba.nazwisko
    nowe_email = input(f"Nowy email (ENTER = {osoba.email}): ") or osoba.email

    wiek_input = input(f"Nowy wiek (ENTER = {osoba.wiek}): ")
    try:
        nowe_wiek = int(wiek_input) if wiek_input.strip() else osoba.wiek
    except ValueError:
        print("[!] Błędny wiek — pozostaje bez zmian.")
        nowe_wiek = osoba.wiek

    osoba.imie = nowe_imie
    osoba.nazwisko = nowe_nazwisko
    osoba.email = nowe_email
    osoba.wiek = nowe_wiek

    print("Dane osoby zaktualizowane.")
    zapisz_do_json()
    zapisz_log(f"Edytowano dane osoby: {osoba.imie} {osoba.nazwisko}")

# Find person by first/last-name & mail
def wyszukaj_osoby():
    fraza = input("Wprowadz fraze do wyszukania (imie, nazwisko, domena e-mail): ").lower()

    wyniki = [
        o for o in osoby
        if fraza in o.imie.lower()
        or fraza in o.nazwisko.lower()
        or fraza in o.email.lower()
    ]

    if not wyniki:
        print(" !X! Nie znaleziono zadnych osob.")
    else:
        print(f"Znaleziono {len(wyniki)} osoby/osob:")
        for o in wyniki:
            print(" -", o)

    zapisz_log(f"Wyszukiwano fraze: '{fraza}' — znaleziono {len(wyniki)} wynikow")

# log change system
from datetime import datetime

def zapisz_log(wiadomosc, plik_log="log.txt"):
    czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(plik_log, "a", encoding="utf-8") as f:
        f.write(f"[{czas}] {wiadomosc}\n")




#############
# Main menu #
#############
def menu():
    while True:
        print("\n========= MENU =========")
        print("1. Wyswietl osoby")
        print("2. Dodaj osobe")
        print("3. Usun osobe po nazwisku")
        print("4. Zapisz do JSON")
        print("5. Wczytaj z JSON")
        print("6. Edytuj osobe po nazwisku")
        print("7. Wyszukaj osoby")
        print("8. Zapisz do CSV")
        print("9. Wczytaj z CSV")
        print("10. Zapisz do TXT")
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
        elif wybor == "6":
            edytuj_osobe()
        elif wybor == "7":
            wyszukaj_osoby()
        elif wybor == "8":
            zapisz_do_csv()
        elif wybor == "9":
            wczytaj_z_csv()
        elif wybor == "10":
            zapisz_do_txt()
        elif wybor == "0":
            print("Zakonczono.")
            break
        else:
            print(" !X! Nieprawidłowa opcja.")

if __name__ == "__main__":
    wczytaj_z_json()
    menu()
