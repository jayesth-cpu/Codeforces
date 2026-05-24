x_row = 0
y_col = 0

for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x_row = i
        y_col = row.index(1)

"""The target position is (2, 2) since the rows and columns are 0-indexed. We can calculate the number of moves required to get to the target position using the Manhattan distance formula."""
moves = abs(x_row - 2) + abs(y_col - 2)
print(moves)
