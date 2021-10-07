# "Long live the king".

# Let's imagine a chessboard, the squares on which are marked with coordinates.
# The coordinates are numbers between 1 and 8 inclusively. The first number
# indicates a column, the second one indicates a row.

# The chess king can stand on any square and can move one step horizontally,
# vertically, or diagonally in any direction within the board.

# The input will contain the coordinates on which the king is located.
# You should figure out and print how many moves the figure can make:
# for example, from the position (1, 8), the king can make
# only 3 moves (right, down, diagonally).


# Answer:

a, b = int(input()), int(input())
count = (1, 8)
if a in count:
    if b in count:
        print(3)
    elif 2 <= b <= 7:
        print(5)
elif 2 <= a <= 7:
    if b in count:
        print(5)
    elif 2 <= b <= 7:
        print(8)
