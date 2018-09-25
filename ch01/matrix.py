from typing import Generic, List, TypeVar

T = TypeVar("T")

# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees.
def rotate_matrix(matrix: List[List[T]]) -> List[List[T]]:
    if len(matrix) == 0:
        return matrix
    num_rows = len(matrix)
    num_columns = len(matrix[0]) # assume they're all the same length
    # create an empty, rotated matrix
    out = [[None for _ in range(num_rows)] for _ in range(num_columns)]
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            inverse_row_idx = num_rows - 1 - row_idx
            out[col_idx][inverse_row_idx] = value # note [col][row] vs. [row][col]
    return out

# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
def zero_matrix(matrix: List[List[T]]) -> None:
    zeroed_rows = set()
    zeroed_cols = set()
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == 0:
                zeroed_rows.add(row_idx)
                zeroed_cols.add(col_idx)
    for row_idx, row in enumerate(matrix):
        for col_idx, _ in enumerate(row):
            if row_idx in zeroed_rows or col_idx in zeroed_cols:
                matrix[row_idx][col_idx] = 0
