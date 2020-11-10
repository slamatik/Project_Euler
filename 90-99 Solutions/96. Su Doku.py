from time import time

class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == '0':
                    return row, col


    def valid_number(self, row, col, num):
        # Check Row
        for c in range(9):
            if self.grid[row][c] == num:
                return False

        # Check Col
        for r in range(9):
            if self.grid[r][col] == num:
                return False

        # Check square
        RC = row // 3
        CC = col // 3
        for r in range(3):
            for c in range(3):
                if self.grid[r + 3 * RC][c + 3 * CC] == num:
                    return False

        return True


    def solve(self):
        if not self.find_empty():
            return self.grid
        row, col = self.find_empty()
        for num in range(1, 10):
            if self.valid_number(row, col, str(num)):
                self.place(row, col, str(num))
                if self.solve():
                    return self.grid
                self.remove(row, col)

    def place(self, row, col, num):
        self.grid[row][col] = num

    def remove(self, row, col):
        self.grid[row][col] = '0'



data = {}
with open('p096_sudoku.txt') as f:
    for line in f:
        if line.startswith('Grid'):
            key = line.rstrip()
            data[key] = []
        else:
            temp_line = list(line.rstrip())
            if temp_line:
                data[key].append(temp_line)

t0 = time()

soltuion = 0
for i in data:
    s = Sudoku(data[i])
    num = int(''.join(s.solve()[0][:3]))
    soltuion += num

print(soltuion)
print(time() - t0)