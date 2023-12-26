def generate_sudoku_grid():
    base = 3
    side = base * base
    grid = [[(base * (r % base) + r // base + c) % side + 1 for c in range(side)] for r in range(side)]
    return grid

def apply_permutations(grid, random_generator):
    rows_permuted = list(range(len(grid)))
    columns_permuted = list(range(len(grid[0])))

    for i in range(len(grid)):
        j = next(random_generator) % len(grid)
        rows_permuted[i], rows_permuted[j] = rows_permuted[j], rows_permuted[i]

    for i in range(len(grid[0])):
        j = next(random_generator) % len(grid[0])
        columns_permuted[i], columns_permuted[j] = columns_permuted[j], columns_permuted[i]

    return [[grid[i][j] for j in columns_permuted] for i in rows_permuted]

def encrypt(plaintext, key, random_generator):
    encrypted_text = ""
    for char in plaintext:
        ascii_val = ord(char)
        row = (ascii_val // 10) % 9
        col = (ascii_val % 10) % 9
        encrypted_text += str(key[row][col])

    return encrypted_text

def decrypt(encrypted_text, key, random_generator):
    decrypted_text = ""
    for digit in encrypted_text:
        row, col = divmod(int(digit) - 1, 9)
        ascii_val = row * 10 + col
        decrypted_text += chr(ascii_val)

    return decrypted_text
