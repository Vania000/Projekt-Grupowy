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
ef print_board():
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