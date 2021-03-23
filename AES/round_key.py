state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    text = ''
    for row in matrix:
        for item in row:
            text += chr(item)

    return text



def add_round_key(s, k):
    new_state = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    for row_index, row in enumerate(s):
        for col_index, item in enumerate(row):
            new_state[row_index][col_index] = s[row_index][col_index] ^ k[row_index][col_index]

    return matrix2bytes(new_state)



print(add_round_key(state, round_key))
