import pygame

class Board:



    boardDimension = 3

    # constructor
    def __init__(self):
        self.ticTacToeGrid = [self.boardDimension][self.boardDimension]
        self.clearBoard(self)

    # clears the board
    def clearBoard(self):
        for rowIndex in self.boardDimension:
            for colIndex in self.boardDimension:
                self.ticTacToeGrid[rowIndex][colIndex] = ""

    # checks if you can set a value on the board
    def canSetValue(self,row,col):
        return self.ticTacToeGrid[row][col] == ""

    # sets value on the tic tac toe board
    def setValue(self,row,col,val):
        self.ticTacToeGrid[row][col] = val

    # check if a player has won
    def checkWin(self,row,col,val):
        return self.__checkHorizontalRows(self,val) or self.__checkVerticalRows(self,val)

    # checks horizontal rows for win
    def __checkHorizontalRows(self,val):
        for rowIndex in self.boardDimension:
            count = 0
            for colIndex in self.boardDimension:
                if self.ticTacToeGrid[rowIndex][colIndex] == val:
                    count = count + 1
            if count == self.boardDimension:
                return True

        return False

    # check vertical rows for win
    def __checkVerticalRows(self, val):
        for colIndex in self.boardDimension:
            count = 0
            for rowIndex in self.boardDimension:
                if self.ticTacToeGrid[rowIndex][colIndex] == val:
                    count = count + 1
            if count == self.boardDimension:
                return True

        return False

    # check backward diagonal for win
    def __checkBackwardDiagonal(self, val):
        rowIndex = 0
        colIndex = 0
        count = 0
        while rowIndex < self.boardDimension and colIndex < self.boardDimension:
            if self.ticTacToeGrid[rowIndex][colIndex] == val:
                count = count + 1
            rowIndex = rowIndex + 1
            colIndex = colIndex + 1

        return count == self.boardDimension

    # check backward diagonal for win
    def __checkForwardDiagonal(self, val):
        rowIndex = self.boardDimension - 1
        colIndex = 0
        count = 0
        while rowIndex > -1 and colIndex < self.boardDimension:
            if self.ticTacToeGrid[rowIndex][colIndex] == val:
                count = count + 1
            rowIndex = rowIndex - 1
            colIndex = colIndex + 1

        return count == self.boardDimension