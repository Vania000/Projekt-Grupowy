import numpy as np
import time
import os

# Ustawienia planszy
m = 21  # liczba wierszy
n = 21  # liczba kolumn
steps = 11000  # liczba kroków (iteracji)

# Stwórz planszę (wszystkie komórki martwe na początku)
board = np.zeros((m, n), dtype=int)  # np.zeros zamiast list comprehension

# Pozycja początkowa mrówki (środek planszy)
ant_row = m // 2
ant_col = n // 2

# Kierunki ruchu mrówki (północ, wschód, południe, zachód)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (dyrowanie w poziomie, w pionie)
# Początkowy kierunek mrówki (początkowo w kierunku północnym)
direction = 0  # 0 - północ, 1 - wschód, 2 - południe, 3 - zachód

# ANSI escape codes for colors
RED = '\033[91m'
RESET = '\033[0m'
BLACK = '\033[48;5;16m'  # Tło czarne
WHITE = '\033[48;5;15m'  # Tło białe

def print_board():
    """Funkcja do wyświetlania planszy w terminalu z czarnymi i białymi polami"""
    os.system('clear')  # Wyczyść ekran przed każdym nowym krokiem
    for row in range(m):
        for col in range(n):
            # Jeśli to komórka z mrówką, wyświetl czerwoną kropkę
            if row == ant_row and col == ant_col:
                print(f"{RED}🟥{RESET}", end="")
            elif board[row][col] == 1:
                # Komórka żywa (czarna)
                print(f"{BLACK}  {RESET}", end="")
            else:
                # Komórka martwa (biała)
                print(f"{WHITE}  {RESET}", end="")
        print()  # Nowa linia po każdym wierszu
    print(f"Rozmiar planszy: {m}x{n}, Krok: {steps} - Ant position: ({ant_row}, {ant_col})")

def resize_board():
    """Funkcja do powiększenia planszy"""
    global board, m, n, ant_row, ant_col  # dodajemy globalne zmienne

    # Sprawdzamy, czy mrówka wyszła poza planszę i powiększamy ją
    if ant_row < 0:  # Jeżeli mrówka wyszła poza górną krawędź
        board = np.vstack([np.zeros((1, n), dtype=int), board])  # Dodajemy nowy wiersz na górze
        m += 1
        ant_row = 0  # Mrówka wchodzi na nowy górny wiersz

    elif ant_row >= m:  # Jeżeli mrówka wyszła poza dolną krawędź
        board = np.vstack([board, np.zeros((1, n), dtype=int)])  # Dodajemy nowy wiersz na dole
        m += 1

    if ant_col < 0:  # Jeżeli mrówka wyszła poza lewą krawędź
        board = np.hstack([np.zeros((m, 1), dtype=int), board])  # Dodajemy nową kolumnę po lewej stronie
        n += 1
        ant_col = 0  # Mrówka wchodzi na nową lewą kolumnę

    elif ant_col >= n:  # Jeżeli mrówka wyszła poza prawą krawędź
        board = np.hstack([board, np.zeros((m, 1), dtype=int)])  # Dodajemy nową kolumnę po prawej stronie
        n += 1


def move_ant():
    """Ruch mrówki w zależności od reguł Langtona"""
    global ant_row, ant_col, direction

    # Jeżeli komórka jest martwa (0), skręcamy w lewo (90° w lewo)
    if board[ant_row][ant_col] == 0:
        direction = (direction - 1) % 4  # Skręt w lewo
        board[ant_row][ant_col] = 1  # Zmiana stanu komórki na żywą
    # Jeżeli komórka jest żywa (1), skręcamy w prawo (90° w prawo)
    else:
        direction = (direction + 1) % 4  # Skręt w prawo
        board[ant_row][ant_col] = 0  # Zmiana stanu komórki na martwą

    # Ruch mrówki na podstawie bieżącego kierunku
    if directions[direction] == (0, 1):  # Wschód
        ant_col += 1
    elif directions[direction] == (1, 0):  # Południe
        ant_row += 1
    elif directions[direction] == (0, -1):  # Zachód
        ant_col -= 1
    elif directions[direction] == (-1, 0):  # Północ
        ant_row -= 1

    # Po wykonaniu ruchu sprawdzamy, czy musimy powiększyć planszę
    resize_board()

def langtons_ant():
    """Symulacja ruchu mrówki przez zadany czas"""
    for _ in range(steps):
        move_ant()
        print_board()
        time.sleep(0.05)  # Opóźnienie dla lepszej wizualizacji

if __name__ == "__main__":
    langtons_ant()
