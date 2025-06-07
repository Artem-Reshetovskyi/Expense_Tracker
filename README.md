# Budżetowy Traker (Expense Tracker)

## Opis projektu

Budżetowy Traker to aplikacja do zarządzania wydatkami, która umożliwia użytkownikom dodawanie, przeglądanie i analizowanie swoich transakcji finansowych. Projekt oparty jest na Django oraz SQL z wykorzystaniem ORM.

## Funkcjonalności

✅ **Zarządzanie wydatkami:**

- Dodawanie wydatków (kwota, kategoria, data, opis)
- Przeglądanie listy wydatków
- Filtrowanie według kategorii i daty

✅ **Analiza wydatków:**

- Podsumowanie miesięczne/tygodniowe
- Wizualizacja danych (wykresy, statystyki)

✅ **Opcjonalne funkcje:**

- Rejestracja i logowanie użytkowników
- Zarządzanie kategoriami wydatków

## Technologie

- **Backend:** Django
- **Baza danych:** SQLite + Django ORM
- **Frontend:** HTML + Bootstrap (lub wbudowane szablony Django)
- **Dodatkowe:** PyInstaller (opcjonalnie dla wersji desktopowej)

## Struktura projektu

```
expense_tracker/
│── app/
│   │── models.py
│   │── routes.py
│   │── templates/
│   │── static/
│── migrations/
│── tests/
│── config.py
│── requirements.txt
│── README.md
│── run.py
```

## Instalacja i uruchomienie

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoj-user/expense-tracker.git
   cd expense-tracker
   ```
2. Utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
3. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```
4. Uruchom aplikację:
   ```bash
   python run.py
   ```

## Dokumentacja

- Dokumentacja generowana za pomocą Sphinx
   Aby zobaczyć dokumentację lokalnie:
   1. Przejdź do folderu `docs/_build/html/`
   2. Otwórz plik `index.html` w przeglądarce
- Kod zgodny ze standardami PEP8
- Diagram klas (opcjonalnie)

## Autorzy

Projekt realizowany w ramach zajęć grupowych. Możliwy podział obowiązków między uczestnikami.

---

**Status projektu:** W trakcie realizacji 🚀

