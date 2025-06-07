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
- **Frontend:** HTML + Bootstrap wbudowane szablony Django
- **Dodatkowe:** PyInstaller (opcjonalnie dla wersji desktopowej)

## Struktura projektu

```
Expense_Tracker/
├── accounts/           # Authentication logic
├── expenses/           # Expense models, views, templates
├── incomes/            # Income logic
├── locale/             # Translation files
├── static/             # CSS, JS, and images
├── templates/          # HTML templates
├── manage.py           # Django management script
└── ...


📦 PyInstaller & Releases
❌ Not yet packaged with PyInstaller.

✅ Will be available soon in GitHub Releases

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

