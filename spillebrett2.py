# coding: utf-8

from celle2 import Cell
import random

# Lager klassen
class GameBoard:

# Instansvariabel settes med parameter rader og kolonner.
# Setter også generasjonsnummer lik 0.
    def __init__(self, rows, columns):
        self._rows = rows
        self._cols = columns
        self._board = self.generate()
        self._generation = 0

# Lager metode som oppretter listen board. For hvert element i kolonner,
# utvider vi listen og returnerer den.
    def generate(self,):
        board = []
        for row in range(self._rows):
            board.append([])
            for column in range(self._cols):
                cell = Cell
                if random.randint(0, 2) == 2:
                    cell.set_alive(self)
                board[row].append(cell)


# Lager metode for å tegne brettet og hente cellestatus fra
# klassen i celle.py. Deretter printe col for hvert element
# i self._board.
    def draw_board(self):
        for i in range(len(self._board)):
            col = ""
            for j in range(len(self._board[i])):
                col = col + self._board[i][j].get_cell_status()
            print(col)
# Printer antall levende celler i brettet og generasjonsnummer,
        print("Number of living cells in board: " + str(self.get_number_of_living_cells()))
        print("Generation: " + str(self._generation))
        print("------------------------------")

# Lager metode for å oppdatere generasjon.
# Setter også generasjon + 1 for å oppdatere generasjonsnummer.
    def update(self):
        resurrecting = []
        dying = []

        for row in range(self._rows):
            for column in range(self._cols):
                if self._board[row][column].is_alive():
                    neighbors = self.find_neighbor(row, column)
                    number = 0
                    for neighbor in neighbors:
                        if neighbor.is_alive():
                            number += 1
                    if number < 2 or number > 3:
                        dying.append([row, column])
                    else:
                        resurrecting.append([row, column])
            for cell in resurrecting:
                cell.set_alive([row, column])
            for cell in dying:
                cell.set_dead([row, column])

        self._generation = self._generation + 1


    def find_neighbor(self, row, col):
        neighborList = []
        for row_step in range(-1, 2):
            for col_step in range(-1, 2):
                validNeighbor = True
            if (row + row_step < 0) or (row + row_step) >= self._rows:
                validNeighbor = False
            if (col + col_step < 0) or (col + col_step >= self._cols):
                validNeighbor = False
            if (row_step == 0) and (col_step == 0):
                validNeighbor = False

            if validNeighbor:
                neighbor = self._board[row + row_step][col + col_step]
                neighborList.append(neighbor)
        return neighborList


# Lager metode for å finne status til naboceller. Setter variabel living lik 0.
# For hvert element fra posisjon -1 til +2 i rader og kolonner lager vi betingelse.
# Vi vil unngå å velge posisjonen for den valgte cellen og heller ikke få
# indekser utenfor listen sin range når vi er på kanten.
    def find_status_of_neighbors(self, row, col):
        living = 0
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if (i != row or j != col) and (i >= 0 and j >= 0) and (i <= self._rows-1 and j <= self._cols-1):
                    if self._board[i][j].is_alive():
                        living = living + 1
        return living


# Lager metode for å finne antall levende celler.
# Setter variabel number lik 0. Går gjennom rader og kolonner for
# å sjekke hvilke celler som er levende. For hver levende celle økes number med 1.
    def get_number_of_living_cells(self):
        number = 0
        for i in range(self._rows):
            for j in range(self._cols):
                if self._board[i][j].is_alive():
                    number = number + 1
        return number