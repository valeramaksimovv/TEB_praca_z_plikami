import json


# v1
class Osoba:
    def __init__(self, imie, nazwisko, wiek, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.email = email

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.wiek} {self.email}"

    def to_dict(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "wiek": self.wiek,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, slownik):
        return cls(
            slownik["imie"],
            slownik["nazwisko"],
            slownik["wiek"],
            slownik["email"]
        )

    def to_list(self):
        return [self.imie, self.nazwisko, self.wiek, self.email]

    @classmethod
    def from_list(cls, lista):
        imie, nazwisko, wiek, email = lista
        return cls(imie, nazwisko, int(wiek), email)