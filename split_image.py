import numpy as np

def split_image(img: np.ndarray, n_rows: int, n_cols: int) -> list:
    '''given a matrix(img) returns a list of n_rows * n_cols (almost) equal size pieces'''
    local_pieces = []

    # row and col sizes for a piece
    row_size = img.shape[0] // n_rows
    col_size = img.shape[1] // n_cols

    # flags to check size matches
    n_rows_not_divisible = img.shape[0] % n_rows != 0
    n_cols_not_divisible = img.shape[1] % n_cols != 0

    for row_offset in range(n_rows):

        if row_offset == n_rows-1 and n_rows_not_divisible:
            row_slice = slice(row_offset*row_size, None)

        else:
            row_slice = slice(row_offset*row_size, (row_offset+1)*row_size)

        for col_offset in range(n_cols):

            if col_offset == n_cols-1 and n_cols_not_divisible:
                col_slice = slice(col_offset*col_size, None)

            else:
                col_slice = slice(col_offset*col_size, (col_offset+1)*col_size)

            local_pieces.append(img[row_slice, col_slice])

    # list of pieces using top->down and left->right notion
    return local_pieces


m = np.array([[1,2,3,4,5,6,7],
              [2,3,4,5,6,7,8],
              [3,4,5,6,7,8,9]])

l = split_image(m, 2, 2)
print(l)
