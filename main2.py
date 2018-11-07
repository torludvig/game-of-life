# coding: utf-8

from spillebrett2 import GameBoard

# Definerer main til å kjøre gameboard med input fra bruker for antall
# rader og kolonner. Får programmet til å kjøre dette med mindre bruker
# skriver q som avslutter programmet.
def main():
    board = GameBoard(int(input("Antall rader: ")), int(input("Antall kolonner: ")))
    temp = ""
    while temp != "q":
        board.draw_board()
        board.update()
        temp = str(raw_input("Press enter for aa fortsette. Skriv q og trykk enter for aa avslutte: "))


main()
