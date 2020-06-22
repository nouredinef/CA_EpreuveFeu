import sys

if len(sys.argv) > 1:
    sudokuFile = sys.argv[1]
else:
    sudokuFile = "./resources/sudoku1.txt"

file = open(sudokuFile)
sudokuTable = file.read().splitlines()
file.close()
sudokuTable.remove("---+---+---")
sudokuTable.remove("---+---+---")

sudokuTable = [list(line.replace('|', '')) for line in sudokuTable]


def get_empty_cases(sudoku):
    emptyCases = []
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == '_':
                emptyCases.append((row, column))
    return emptyCases


def get_row_numbers(position, sudoku, keep_position=False):
    result = sudoku[position[0]][:]
    if keep_position:
        return result
    else:
        result.pop(position[1])
        return result


def get_column_numbers(position, sudoku, keep_position=False):
    result = [row[position[1]] for row in sudoku]
    if keep_position:
        return result
    else:
        result.pop(position[0])
        return result


def get_neighbour_numbers(position, sudoku, keep_position=False):
    result = []
    row = position[0]
    col = position[1]
    if ((row < 3) & (col < 3)):
        for i in range(3):
            for j in range(3):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    elif ((row >= 3) & (row < 6) & (col < 3)):
        for i in range(3, 6):
            for j in range(3):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    elif ((row >= 6) & (col < 3)):
        for i in range(6, 9):
            for j in range(3):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    # 2nd column
    elif ((row < 3) & (col >= 3) & (col < 6)):
        for i in range(3):
            for j in range(3, 6):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    elif ((row >= 3) & (row < 6) & (col >= 3) & (col < 6)):
        for i in range(3, 6):
            for j in range(3, 6):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    elif ((row >= 6) & (col >= 3) & (col < 6)):
        for i in range(6, 9):
            for j in range(3, 6):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    # 3rd column
    elif ((row < 3) & (col >= 6)):
        for i in range(3):
            for j in range(6, 9):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    elif ((row >= 3) & (row < 6) & (col >= 6)):
        for i in range(3, 6):
            for j in range(6, 9):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    elif ((row >= 6) & (col >= 6)):
        for i in range(6, 9):
            for j in range(6, 9):
                if ((i == row) & (j == col) & (not keep_position)):
                    continue
                else:
                    result.append(sudoku[i][j])
        return result
    else:
        return []


def get_possible_numbers(position, sudoku):
    lin = get_row_numbers(position, sudoku)
    col = get_column_numbers(position, sudoku)
    nei = get_neighbour_numbers(position, sudoku)
    numbers = [i for i in range(1, 10, 1)]

    for i in range(8):
        for j in numbers:
            if lin[i] == str(j):
                numbers.remove(j)
                continue
            if col[i] == str(j):
                numbers.remove(j)
                continue
            if nei[i] == str(j):
                numbers.remove(j)
                continue
    return numbers


def solve_sudoku(sudoku):
    empty_positions = get_empty_cases(sudoku)
    while len(empty_positions) != 0:
        empty_positions = get_empty_cases(sudoku)
        for pos in empty_positions:
            possible_sol = get_possible_numbers(pos, sudoku)
            if len(possible_sol) == 1:
                sudoku[pos[0]][pos[1]] = str(possible_sol[0])
            else:

                continue
    return sudoku


def write_sudoku_to_file(sudoku, base_filename=sudokuFile):
    filename = base_filename + "_solution.txt"
    solution_file = open(filename, mode='w')
    i=0
    for line in sudoku:
        i += 1
        solution_file.write(''.join(line[0:3]) + '|' + ''.join(line[3:6]) + '|' + ''.join(line[6:9]) + "\n")
        if (i == 3) | (i == 6):
            solution_file.write('---+---+---\n')
    solution_file.close()


# write_sudoku_to_file(solve_sudoku(sudokuTable))

for line in sudokuTable:
    print(''.join(line[0:3]), '|', ''.join(line[3:6]))


print(solve_sudoku(sudokuTable))
# Tests

# print("Empty cases : ", get_empty_cases(sudokuTable))
#
# for pos in get_empty_cases(sudokuTable):
#     print("---------------------------")
#     print("Testing for position ", pos, ": ")
#     print("Row numbers: ", get_row_numbers(pos, sudokuTable))
#     print("Col numbers: ", get_column_numbers(pos, sudokuTable))
#     print("Neighbour numbers: ", get_neighbour_numbers(pos, sudokuTable))
#     print("Possible Numbers: ", get_possible_numbers(pos, sudokuTable))
#     print("End...")

# print("Rows numbers (0,7): ", get_row_numbers((0, 7), sudokuTable, True))
# print("Column numbers (2,4): ", get_column_numbers((2, 4), sudokuTable, True))
# print("Neighbor numbers (1,1): ", get_neighbour_numbers((1, 1), sudokuTable))
# print("Neighbor numbers (3,0): ", get_neighbour_numbers((3, 0), sudokuTable))
# print("Neighbor numbers (6,0): ", get_neighbour_numbers((6, 0), sudokuTable))
# print("Neighbor numbers (0,3): ", get_neighbour_numbers((0, 3), sudokuTable))
# print("Neighbor numbers (3,3): ", get_neighbour_numbers((3, 3), sudokuTable))
# print("Neighbor numbers (6,3): ", get_neighbour_numbers((6, 3), sudokuTable))
# print("Neighbor numbers (0,6): ", get_neighbour_numbers((0, 6), sudokuTable))
# print("Neighbor numbers (3,6): ", get_neighbour_numbers((3, 6), sudokuTable))
# print("Neighbor numbers (6,6): ", get_neighbour_numbers((6, 6), sudokuTable))
