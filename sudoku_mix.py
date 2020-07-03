import sys
import time
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    sudokuFile = sys.argv[1]
else:
    sudokuFile = "./resources/sudoku3.txt"

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


def get_neighbour_numbers(position, sudoku, keep_position=False, result_as_map=False):
    if result_as_map:
        result = {}
    else:
        result = []
    row = position[0]
    col = position[1]
    if int(col / 3) == 0:
        col_range = range(3)
    elif int(col / 3) == 1:
        col_range = range(3, 6)
    elif int(col / 3) == 2:
        col_range = range(6, 9)
    else:
        return []
    if int(row / 3) == 0:
        row_range = range(3)
    elif int(row / 3) == 1:
        row_range = range(3, 6)
    elif int(row / 3) == 2:
        row_range = range(6, 9)
    else:
        return []
    for i in row_range:
        for j in col_range:
            if (i == row) & (j == col) & (not keep_position):
                continue
            else:
                if result_as_map:
                    result[(i, j)] = sudoku[i][j]
                else:
                    result.append(sudoku[i][j])
    return result

def fill_sudoku(original_sudoku):
    sudoku = [line.copy() for line in original_sudoku]
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == '_':
                for i in range(1, 10):
                    sudoku[x][y] = str(i)
                    if str(i) not in get_row_numbers((x, y), sudoku) +\
                            get_column_numbers((x, y), sudoku) +\
                            get_neighbour_numbers((x, y), sudoku):
                        sudoku = fill_sudoku([line.copy() for line in sudoku])
                        if sudoku is not False:
                            return sudoku
                        else:
                            sudoku = original_sudoku
                return False
    return sudoku


def fill_sudoku_elimination_indirecte(sudoku):
    case_filled = True
    while case_filled:
        case_filled = False
        for i in range(1, 10):
            for pos in get_empty_cases(sudoku):
                if str(i) in (get_row_numbers(pos, sudoku) +
                              get_column_numbers(pos, sudoku) +
                              get_neighbour_numbers(pos, sudoku)):
                    sudoku[pos[0]][pos[1]] = 'X'
                    continue
            empty_cases = get_empty_cases(sudoku)
            empty_nei = True
            while empty_nei:
                empty_nei = False
                empty_row = False
                empty_col = False
                visited_pos = []
                for pos in empty_cases:
                    if pos in visited_pos:
                        continue
                    empty_nei_pos = [pos]
                    visited_pos.append(pos)
                    neighbours = get_neighbour_numbers(pos, sudoku, False, True)
                    for nei_pos in list(neighbours):
                        if neighbours[nei_pos] != '_':
                            continue
                        visited_pos.extend(list(neighbours))
                        if (nei_pos[0] == pos[0]) & (nei_pos[1] != pos[1]) & (not empty_col):
                            empty_row = True
                            empty_nei = True
                            empty_nei_pos.append(nei_pos)
                        elif (nei_pos[1] == pos[1]) & (nei_pos[0] != pos[0]) & (not empty_row):
                            empty_col = True
                            empty_nei = True
                            empty_nei_pos.append(nei_pos)
                        else:
                            empty_col = False
                            empty_row = False
                            empty_nei = False
                            break
                    if empty_nei:
                        changed_case = False
                        if empty_row:
                            for n in range(9):
                                if (pos[0], n) in empty_nei_pos:
                                    continue
                                if sudoku[pos[0]][n] == '_':
                                    sudoku[pos[0]][n] = 'X'
                                    changed_case = True
                        if empty_col:
                            for n in range(9):
                                if (n, pos[1]) in empty_nei_pos:
                                    continue
                                if sudoku[n][pos[1]] == '_':
                                    sudoku[n][pos[1]] = 'X'
                                    changed_case = True
                        if not changed_case:
                            empty_nei = False
            for pos in get_empty_cases(sudoku):
                if ('_' not in get_neighbour_numbers(pos, sudoku)) | \
                        ('_' not in get_column_numbers(pos, sudoku)) | \
                        ('_' not in get_row_numbers(pos, sudoku)):
                    sudoku[pos[0]][pos[1]] = str(i)
                    case_filled = True
                    break
            for j in range(9):
                for k in range(9):
                    if sudoku[j][k] == 'X':
                        sudoku[j][k] = '_'
    return sudoku


def write_sudoku_to_file(sudoku, base_filename=sudokuFile):
    filename = base_filename + "_solution.txt"
    solution_file = open(filename, mode='w')
    i = 0
    for line in sudoku:
        i += 1
        solution_file.write(''.join(line[0:3]) + '|' + ''.join(line[3:6]) + '|' + ''.join(line[6:9]) + "\n")
        if (i == 3) | (i == 6):
            solution_file.write('---+---+---\n')
    solution_file.close()


def validate_solution(sudoku):
    for x in range(9):
        for y in range(9):
            pos = (x, y)
            if sudoku[x][y] in (get_row_numbers(pos, sudoku) +
                                get_column_numbers(pos, sudoku) +
                                get_neighbour_numbers(pos, sudoku)):
                return False
    return True


def print_sudoku(sudoku):
    for i, line in enumerate(sudoku):
        print(''.join(line[0:3]) + '|' + ''.join(line[3:6]) + '|' + ''.join(line[6:9]))
        if (i == 2) | (i == 5):
            print('---+---+---')


# write_sudoku_to_file(solve_sudoku(sudokuTable))

# print("Tests copy arrays")
# print("Table id", id(sudokuTable))
# print("each array of table:")
# for i, array in enumerate(sudokuTable):
#     print(i, id(array))
#
# copyTable = sudokuTable.copy()
# print("Copy id", id(copyTable))
# print("each array of Copy:")
# for i, array in enumerate(copyTable):
#     print(i, id(array))



print("Sudoku présenté :")
print_sudoku(sudokuTable)
print('********************************')

sudokuSolved = fill_sudoku_elimination_indirecte(sudokuTable)

valid = validate_solution(sudokuSolved)
if valid:
    write_sudoku_to_file(sudokuSolved)
    print('The solution is valid and saved!')
else:
    sudokuSolved = fill_sudoku(sudokuSolved)
    valid = validate_solution(sudokuSolved)
    if valid:
        write_sudoku_to_file(sudokuSolved)
        print('The solution is valid and saved!')


print('********************************')
print("Sudoku rempli :")
print_sudoku(sudokuSolved)



valid = validate_solution(sudokuSolved)
if valid:
    write_sudoku_to_file(sudokuSolved)
    print('The solution is valid and saved!')
