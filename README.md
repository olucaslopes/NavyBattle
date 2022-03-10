# NavyBattle
A Software Engineering college project

## Motivation:

During a Software Engineering class I was exposed to the a Naval Battle Puzzle:

It consists of finding the ships hidden along a board. In this version, there are some constraints:

- the board must have 5 rows and 5 columns
- each ship in the board must lie into one single cell
- we are given the number of ships in each row and in each column

<aside>
💡 Our goal is to find all valid solutions to this play (if any) using Python and also build a visualization of the board.

</aside>

## How the code works:

2 classes where built. 

The **Board** class which stores a board and when printed show a representation of the board. 

The **NavyBattle** class generate all valid boards iterate over the boards in a optimized way to find the right solution - first looking only to rows, and then to columns.

### Requirements

This program requires Python to run. You can download Python [here](https://www.python.org/downloads/)

This program also requires the Pandas library to work. After installing Python, you can easily install it using the following code in your terminal:

```
$ python -m pip install pandas
```

## Usage example:

```python
row_info = [0, 2, 1, 1, 1]  # Defining the number of ships in each row
col_info = [1, 1, 3, 0 , 0]  # Defining the number of ships in each column

battle = NavyBattle(row_info, col_info)  # Creating an instance of a game

battle.solve_boards()  # Finding and printing the valid solutions
```

**Output:**
<p align="center">
    <img align='center' alt="NavyBattle solutions representation" src='https://i.imgur.com/KKbe06N.png'/>