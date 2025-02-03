import numpy as np
import time
import os

def poprawna_wartosc(prompt):
    """
    Funkcja pobiera od użytkownika wartość i sprawdza, czy jest ona liczbą naturalną, np.:
    Podaj liczbę wierszy: -1
    Błąd: Podaj liczbę naturalną większą od 0.
    Podaj liczbę wierszy: 25
    Liczba iteracji dowolna, liczba kolumn i wierszy zalecana od 10 do 50 (by uniknąć problemów z wyświetlaniem)
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Błąd: Podaj liczbę naturalną większą od 0.")
            else:
                return value
        except ValueError:
            print("Błąd: Podana wartość nie jest liczbą całkowitą.")

m = poprawna_wartosc("Podaj liczbę wierszy: ")
n = poprawna_wartosc("Podaj liczbę kolumn: ")
steps = poprawna_wartosc("Podaj liczbę iteracji: ")

"""Tworzenie planszy"""
board = np.zeros((m, n), dtype=int)

"""Pozycja początkowa mrówki"""
ant_row = m // 2
ant_col = n // 2

"""Kierunki ruchu mrówki"""
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

RED = '\033[91m'
RESET = '\033[0m'
BLACK = '\033[48;5;16m'
WHITE = '\033[48;5;15m'
def print_board():
    """Funkcja do wyświetlania planszy w terminalu z czarnymi i białymi polami"""
    os.system('clear')
    for row in range(m):
        for col in range(n):
            if row == ant_row and col == ant_col:
                print(f"{RED}🟥{RESET}", end="")
            elif board[row][col] == 1:
                print(f"{BLACK}  {RESET}", end="")
            else:
                print(f"{WHITE}  {RESET}", end="")
        print()
    print(f"Rozmiar planszy: {m}x{n}, Krok: {steps} - Ant position: ({ant_row}, {ant_col})")
def resize_board():
    """Funkcja do powiększenia planszy, jeśli mrówka zacznie przekraczać jej krawędzie"""
    global board, m, n, ant_row, ant_col

    if ant_row < 0:
        board = np.vstack([np.zeros((1, n), dtype=int), board])
        m += 1
        ant_row = 0

    elif ant_row >= m:
        board = np.vstack([board, np.zeros((1, n), dtype=int)])
        m += 1

    if ant_col < 0:
        board = np.hstack([np.zeros((m, 1), dtype=int), board])
        n += 1
        ant_col = 0

    elif ant_col >= n:
        board = np.hstack([board, np.zeros((m, 1), dtype=int)])
        n += 1
        def move_ant():
    """Ruch mrówki w zależności od tego, na jakim polu stoi"""
    global ant_row, ant_col, direction

    if board[ant_row][ant_col] == 0:
        direction = (direction - 1) % 4
        board[ant_row][ant_col] = 1
    else:
        direction = (direction + 1) % 4
        board[ant_row][ant_col] = 0
 if directions[direction] == (0, 1):
        ant_col += 1
    elif directions[direction] == (1, 0):
        ant_row += 1
    elif directions[direction] == (0, -1):
        ant_col -= 1
    elif directions[direction] == (-1, 0):
        ant_row -= 1

    resize_board()

def langtons_ant():
    """Symulacja ruchu mrówki przez zadany czas"""
    for _ in range(steps):
        move_ant()
        print_board()
        time.sleep(0.05)

if __name__ == "__main__":
    langtons_ant()
