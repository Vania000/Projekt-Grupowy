

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