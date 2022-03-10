# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:21:35 2022

@author: lucas.amorim
"""

import pandas as pd
from itertools import permutations


class NavyBattle:
    """
    The Navy Battle game generator global representation
    """

    def __init__(self, row_counts, col_counts):
        """Take the number of ships in each row and column of the board

        Parameters
        ----------
        row_counts: list or str
            iterable of length 5
        col_counts: list or str
            iterable of length 5

        Notes
        -----
        row_counts and col_counts must be of the length 5
        """
        if sum(row_counts) != sum(col_counts):
            raise ValueError(
                'When counting by rows or counting by cols you must have the same number of total ships'
            )
        if len(row_counts) != 5 or len(col_counts) != 5:
            raise ValueError('row_counts and col_counts must be of length 5')

        self.row_counts = row_counts
        self.col_counts = col_counts

        self.has_solution = None

        self.solution = None

    def _gen_boards_by_row(self) -> list:
        """
        Generates all possible boards looking only to the rows constraints
        """

        # Generating a reference instance of a board to iterate
        instance = []
        for index, navy_count in enumerate(self.row_counts):
            navies = [True, ] * navy_count

            sea_count = len(self.row_counts) - navy_count
            sea = [False, ] * sea_count

            instance.append(
                navies + sea
            )

        # Creating matrix aggregating the permutations of each row
        matrix = []

        for row in instance:
            row_permutations = set(permutations(row, len(row)))
            matrix.append(row_permutations)

        # Creating a list of boards with all
        # possible boards according the rows constraints.
        boards = []

        for lst1 in matrix[0]:
            for lst2 in matrix[1]:
                for lst3 in matrix[2]:
                    for lst4 in matrix[3]:
                        for lst5 in matrix[4]:
                            boards.append((lst1, lst2, lst3, lst4, lst5))

        return boards

    def _solve_boards(self, lst_boards) -> None:
        """
        Filter the generated boards according the cols constraints
        """
        # Create board instances
        boards = [Board(b) for b in lst_boards]

        # Aggregate valid solutions
        solutions = []
        for b in boards:
            for index, count in enumerate(self.col_counts):
                if b.ships_in_col(index) != count:
                    break
            else:
                solutions.append(b)

        if len(solutions) > 0:
            self.has_solution = True
            self.solution = solutions
        else:
            self.has_solution = False

        self.solution = solutions

    def solve_boards(self, print_solutions=True) -> None:
        """Print how many solutions has a specified board.

        Parameters
        ----------
        print_solutions : bool
            Whether of not to print the solutions of the board
        """
        boards = self._gen_boards_by_row()

        self._solve_boards(boards)

        if self.has_solution:
            print(f'This setup has {len(self.solution)} solutions')
            if print_solutions:
                print()
                for i, sol in enumerate(self.solution):
                    print(f'Solution {i + 1}:\n')
                    print(sol)
        else:
            print('This setup has NO SOLUTION.')


class Board:
    """
    The Naval battle game board representation
    """

    def __init__(self, iterable5x5):
        """
        Initialize a 5x5 board with indexes
        ranging from 0 to 4
        """
        df = pd.DataFrame(iterable5x5)

        assert len(df.columns) == 5
        assert len(df.index) == 5

        self.df = df

    def get_board(self):
        """
        Returns a game board as a DataFrame
        """
        return self.df.copy()

    def ships_in_row(self, row_number):
        """
        Returns the number of ships in a row
        """
        return self.df.loc[row_number].sum()

    def ships_in_col(self, col_number):
        """
        Return the number of ships in a column
        """
        return self.df[col_number].sum()

    def is_a_ship(self, row_number, col_number):
        """
        Returns True if there is a ship
        in the given position and False
        otherwise.
        """
        return self.df.loc[row_number, col_number]

    def __str__(self):
        chac = ''
        for row in range(5):
            for col in range(5):
                cell = self.df.iloc[row, col]
                chac += '🚢' if cell else '⚓'
            chac += '\n'

        return chac


if __name__ == '__main__':
    # row_info = [0, 2, 1, 1, 1]
    # col_info = [1, 1, 3, 0 , 0]

    row_info = [2, 0, 1, 2, 1]
    col_info = [0, 4, 1, 1, 0]

    battle = NavyBattle(row_info, col_info)

    battle.solve_boards()
