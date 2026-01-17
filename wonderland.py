"""
CSCA08: Winter 2024 -- Assignment 2: Wacky Wonderland

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

# deepcopy() is used to make sure we can easily clone arrays.
# An example of how it's used is given on the assignment handout.
from copy import deepcopy

# The constants below are provided as test data and can be
# modified and used inside your docstrings to test your functions.

TEST_ACC_NUM_A = [1, 9, 4, 5, 5, 7, 2]

SAMPLE_MATRIX_A = [
    [3, 4, 5],
    [8, 8, 8],
    [1, 0, 5],
    [1, 8, 7]
]

SAMPLE_MATRIX_A_T = [
    [3, 8, 1, 1],
    [4, 8, 0, 8],
    [5, 8, 5, 7],
]

SAMPLE_MATRIX_B = [
    [3, 4, 5, 2, 9, 1, 5, 3, 2, 8],
    [8, 8, 8, 9, 2, 7, 8, 7, 3, 5],
    [1, 0, 5, 2, 4, 9, 4, 0, 3, 8],
    [1, 8, 7, 5, 6, 2, 4, 9, 7, 1],
    [6, 3, 3, 8, 7, 3, 3, 2, 2, 9],
    [0, 2, 4, 5, 1, 9, 4, 2, 8, 5],
    [9, 6, 7, 0, 2, 4, 1, 0, 2, 1],
    [1, 5, 9, 0, 2, 4, 2, 2, 4, 6],
    [5, 5, 4, 9, 3, 1, 2, 3, 4, 0],
    [2, 6, 7, 9, 9, 5, 3, 8, 2, 2]
]

#############################################################
### PART 1 : Account Numbers
#############################################################

def sum_of_digits(number: int) -> int:
    '''
    Given a non-negative integer 'number', return the sum of all its digits.

    Preconditions: number >= 0

    >>> sum_of_digits(1234)
    10
    >>> sum_of_digits(8888)
    32
    '''
    tot = 0
    for i in str(number):
        tot += int(i)
    return tot


def is_valid_account(num_array: list[int]) -> bool:
    '''Given a list of integers, return whether or not it is a valid account.

    The list num_array is divided into three parts. The second last and last
    integers are the multiplier and the modulo respectively. The remaining
    elements make up the payload in the same sequence as in num_array. Starting
    from the rightmost integer of the payload and moving left, every second
    integer is multiplied by the multiplier. Then, split all the integers in
    payload into individual digits and take their sum. Take the sum of all sums.
    The account number is valid if and only if the resulting sum modulo 10
    equals to the modulo variable. Return True if it is valid, False otherwise.

    Preconditions: len(num_array) >= 3
                   num_array contains only non-negative integers

    >>> is_valid_account([1, 9, 4, 5, 5, 7, 2])
    False
    >>> is_valid_account([3, 7, 6, 4, 7, 9, 0, 6])
    True
    '''
    mult = num_array[-2]
    mod = num_array[-1]
    payload = num_array[:-2]
    for i in range(0,len(payload),2):
        payload[len(payload)-1-i] *= mult
    sums = 0
    for num in payload:
        sums += sum_of_digits(num)
    return sums % 10 == mod


#############################################################
### PART 2 : Memory Trail
#############################################################

def memory_median(num_array: list[int]) -> float:
    '''Given a list of integers, return the middle value of its sorted version.

    If the list has an even number of elements, sort the list and return the
    average of the two middle numbers.

    >>> memory_median([5, 7, 9, 8, 2, 1, 6, 3])
    5.5
    >>> memory_median([6, 5, 7, 3, 2, 1, 9])
    5.0
    '''
    sortl = deepcopy(num_array)
    sortl.sort()
    pos = len(sortl) // 2
    med = (sortl[pos] + sortl[len(sortl)-1-pos]) / 2
    return med


def memory_sequence(num_array: list[int]) -> list[int]:
    '''Given a list of integers, return a modified version of the list.

    Modify by deleting any duplicated numbers and retaining the one closest to
    the beginning of the list.

    >>> memory_sequence([1, 1, 3, 2, 2, 4, 5, 2])
    [1, 3, 2, 4, 5]
    >>> memory_sequence([1, 1, 1, 3, 4, 1, 1, 6])
    [1, 3, 4, 6]
    '''
    newlist = []
    for num in num_array:
        if num not in newlist:
            newlist.append(num)
    return newlist


def memory_count(num_array: list[int], recall_array: list[int]) -> list[int]:
    '''Given two lists of integers num_array and recall_array, return a list of
    integers indicating how many times each integer in recall_array occurs in
    num_array.

    >>> memory_count([1, 1, 3, 2, 2, 4, 5, 2], [1, 5, 7, 2])
    [2, 1, 0, 3]
    >>> memory_count([1, 2, 4, 6, 7, 7, 7, 7], [7, 3, 6, 9])
    [4, 0, 1, 0]
    '''
    occur_array = []
    for key in recall_array:
        count = 0
        for num in num_array:
            if num == key:
                count += 1
        occur_array.append(count)
    return occur_array


#############################################################
### PART 3 : Numbers Search
#############################################################


def swap_around(matrix: list[list[int]]) -> list[list[int]]:
    '''Given an integer matrix of size row * col , return a new integer matrix
    of size col * row that swaps the rows and columns of the original.

    Preconditions: len(matrix) == row
                   len(matrix[i]) == col, 0 <= i < row

    >>> swap_around(SAMPLE_MATRIX_A) == SAMPLE_MATRIX_A_T
    True
    >>> swap_around([[0, 0], [1, 2], [3, 4]])
    [[0, 1, 3], [0, 2, 4]]
    '''
    rows = len(matrix)
    cols = len(matrix[0])
    new = []
    for num in matrix[0]:
        new.append([num])
    for row in range(1, rows):
        for col in range(cols):
            new[col].append(matrix[row][col])
    return new


def search_list(num_list: list[int], series: list[int]) -> int:
    '''Given two lists of integers num_list and series, return the position of
    the first occurence of series or its reversed version in num_list.

    >>> SAMPLE_LIST = [3, 4, 5, 8, 8, 8, 1, 0, 5]
    >>> search_list(SAMPLE_LIST, [5, 8, 8])
    2
    >>> search_list(SAMPLE_LIST, [8, 8, 5])
    2
    '''
    pos1 = -1
    pos2 = -1
    rev = deepcopy(series)
    rev.reverse()
    for num in range(len(num_list) - len(series) + 1):
        if num_list[num: num + len(series)] == series:
            pos1 = num
            break
    for num in range(len(num_list) - len(series) + 1):
        if num_list[num: num + len(series)] == rev:
            pos2 = num
            break
    if pos1 > -1:
        if pos1 <= pos2:
            return pos1
        if pos2 > -1:
            return pos2
        return pos1
    return pos2


def search_rows(matrix: list[list[int]], series: list[int]) -> bool:
    '''Given an integer matrix matrix of size N*M and a list of integers series,
    return whether or not series or its reversed version is in any of the rows
    of matrix.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N

    >>> search_rows(SAMPLE_MATRIX_B, [8, 7, 3, 3])
    True
    >>> search_rows(SAMPLE_MATRIX_B, [4, 3, 2, 1])
    True
    >>> search_rows(SAMPLE_MATRIX_B, [1, 1, 1])
    False
    '''
    for row in matrix:
        if search_list(row, series) != -1:
            return True
    return False


def search_columns(matrix: list[list[int]], series: list[int]) -> bool:
    '''Given an integer matrix matrix of size N*M and a list of integers series,
    return whether or not series or its reversed version is in any of the
    columns of matrix.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N

    >>> search_columns(SAMPLE_MATRIX_B, [3, 9, 4, 4])
    True
    >>> search_columns(SAMPLE_MATRIX_B, [7, 4, 3, 7])
    True
    >>> search_columns(SAMPLE_MATRIX_B, [1, 2, 3, 4])
    False
    '''
    swapped = swap_around(matrix)
    for row in swapped:
        if search_list(row, series) != -1:
            return True
    return False


def search_diagonals(matrix: list[list[int]], series: list[int]) -> bool:
    '''Given an integer matrix matrix of size N * M and an integer list series,
    return whether or not series or its reversed version occurs in the diagonals
    of the matrix. If no matches are found, return False.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N

    >>> search_diagonals(SAMPLE_MATRIX_B, [3, 1, 0, 9, 5])
    True
    >>> search_diagonals(SAMPLE_MATRIX_B, [9, 9, 6, 0])
    True
    >>> search_diagonals(SAMPLE_MATRIX_B, [1, 2, 3, 4])
    False
    '''
    matri = deepcopy(matrix)
    diag1 = []
    diag2 = []
    row = len(matrix)
    col = len(matrix[0])
    for a_row in range(row):
        line = []
        a_col = 0
        while a_row >= 0 and a_col < col:
            line.append(matri[a_row][a_col])
            a_row -= 1
            a_col += 1
        diag1.append(line)
    for a_col in range(1, col):
        line = []
        a_row = row - 1
        while a_row >= 0 and a_col < col:
            line.append(matri[a_row][a_col])
            a_row -= 1
            a_col += 1
        diag1.append(line)
    for a_row in range(row):
        line = []
        a_col = 0
        while a_row < row and a_col < col:
            line.append(matri[a_row][a_col])
            a_row += 1
            a_col += 1
        diag2.append(line)
    for a_col in range(1, col):
        line = []
        a_row = 0
        while a_row < row and a_col < col:
            line.append(matri[a_row][a_col])
            a_row += 1
            a_col += 1
        diag2.append(line)
    in1 = search_rows(diag1, series)
    in2 = search_rows(diag2, series)
    return in1 or in2


def validate_coordinates(matrix: list[list[int]], row_idx: int,
                         col_idx: int, series: list[int]) -> bool:
    '''Given an integer matrix matrix of size N * M, integers row_idx and
    col_idx, and an integer list series, return whether or not series or its
    reversed version occurs at and overlaps the element in the row_idx row and
    col_idx column of matrix, either via row, column, or diagonal. Return False
    if no matches are found.

    preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N
                   row_idx < N
                   col_matrix < M

    >>> validate_coordinates(SAMPLE_MATRIX_B, 4, 3, [4, 1, 8, 7, 0, 8])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_B, 5, 7, [7, 0, 9, 2, 2])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_B, 9, 0, [7, 9, 9, 5])
    False
    >>> validate_coordinates([[1, 1], [2, 2], [3, 3]], 1, 0, [2, 3])
    True
    '''
    row = len(matrix)
    col = len(matrix[0])
    num = len(series)
    r_line = matrix[row_idx][max(0, col_idx - num + 1): min(col, col_idx + num)]
    swap = swap_around(matrix)
    c_line = swap[col_idx][max(0, row_idx - num + 1): min(row, row_idx + num)]
    di1 = []
    di2 = []
    down_right = min(num, row - row_idx, col - col_idx)
    for index in range(- min(num, row_idx +1, col_idx + 1) + 1, down_right):
        di1.append(matrix[row_idx + index][col_idx + index])
    up_right = min(num, row_idx +1, col - col_idx)
    for index in range(- min(num, row - row_idx, col_idx + 1) + 1, up_right):
        di2.append(matrix[row_idx - index][col_idx + index])
    return search_rows([r_line, c_line, di1, di2], series)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
