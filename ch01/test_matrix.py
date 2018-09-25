import ch01.matrix as m

def test_rotate_matrix():
    matrix = [
        [10],
        [20],
    ]
    rotated = [
        [20, 10],
    ]
    assert m.rotate_matrix(matrix) == rotated

    matrix = [
        [10, 20, 30],
    ]
    rotated = [
        [10],
        [20],
        [30],
    ]
    assert m.rotate_matrix(matrix) == rotated

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    rotated = [
        [4, 1],
        [5, 2],
        [6, 3],
    ]
    assert m.rotate_matrix(matrix) == rotated

def test_rotate_matrix_edge_cases():
    assert m.rotate_matrix([]) == []
    assert m.rotate_matrix([[]]) == [] # 1 row, 0 columns // 0 rows, therefore can't represent columns
    assert m.rotate_matrix([[], []]) == [] # 2 rows, 0 columns // 0 rows, therefore can't represent columns

def test_zero_matrix():
    matrix = [
        [1,  2,  3,  0,  5],
        [6,  7,  0,  8,  9],
        [10, 11, 12, 13, 14],
    ]
    zeroed_matrix = [
        [0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0],
        [10, 11, 0,  0,  14],
    ]
    m.zero_matrix(matrix)
    assert matrix == zeroed_matrix

def test_zero_matrix_edge_cases():
    # nothing to zero
    matrix = [[1, 2, 3], [4, 5, 6],]
    m.zero_matrix(matrix)
    assert matrix == [[1, 2, 3], [4, 5, 6],]

    # empty rows
    matrix = [[], [],]
    m.zero_matrix(matrix)
    assert matrix == [[], [],]

    # empty matrix
    matrix = []
    m.zero_matrix(matrix)
    assert matrix == []
