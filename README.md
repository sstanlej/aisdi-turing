# Turing Machine Simulator

Prosty i funkcjonalny symulator **Maszyny Turinga** zaimplementowany w języku Python. Program pozwala na definiowanie dowolnych automatów poprzez zewnętrzne pliki z tablicą przejść oraz wizualizację pracy maszyny krok po kroku w konsoli.



## Funkcjonalności
* Wizualizacja procesu**: Wyświetlanie aktualnej zawartości taśmy, stanu automatu oraz graficzne wskazanie pozycji głowicy (`^`).
* Elastyczna konfiguracja**: Możliwość definiowania własnych algorytmów bez modyfikacji kodu źródłowego.
* Logika zatrzymania**: Maszyna kończy pracę po osiągnięciu stanu zaczynającego się od słowa `halt` lub w przypadku braku zdefiniowanej reguły dla danej kombinacji (stan, symbol).

## Instrukcja uruchomienia

Program uruchamiany jest z wiersza poleceń z dwoma argumentami:
1. Początkowa zawartość taśmy.
2. Ścieżka do pliku z tabelą przejść.

```bash
python machine.py <input_tape> <transitions_file>
# Przykład:
python machine.py 10110 transitions.txt
```
