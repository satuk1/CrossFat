# Instrukcje instalacji i uruchomienia aplikacji Django

## Instalacja Django:

1. **Sprawdź wersję Pythona**: Upewnij się, że masz zainstalowaną odpowiednią wersję Pythona. Django współpracuje z Pythonem w wersji 3.6 lub nowszej. Możesz sprawdzić wersję Pythona wpisując w terminalu lub wierszu poleceń:
```python
  python --version
```
2. Zainstalowanie oprogramowania PyCharm.

3. **Zainstaluj Django**: Możesz zainstalować Django za pomocą narzędzia `pip`, które jest standardowym menedżerem pakietów dla Pythona. Wpisz w terminalu lub wierszu poleceń:
pip install django
   ```python
   pip install django

4. Przechodzimy do sklonowania repozytorium gitguba:
   ```python
   git clone https://github.com/satuk1/CrossFat.git

5. Przechodzimy w pycharmie do katalogu aplikacji, w którym znajduję się plik manage.py, do przechodzenia miedzy katalogami używami polecania
   ```python
   cd ...

6. Pobieramy wszystkie modele do bazy danych
   ```python
   python manage.py makemigrations
   python manage.py migrate

7. Zapełniamy baze danych danymi
   ```python
   python .\dodaj_dane.py

 8. Do włączenia aplikacji pozostaje nam tylko uruchomic server
    ```python
    python manage.py startserver

