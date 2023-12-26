/*EALGO*/

import random

def generate_sudoku_grid():
    base = 3
    side = base * base
    grid = [[(base * (r % base) + r // base + c) % side + 1 for c in range(side)] for r in range(side)]
    return grid

def apply_permutations(grid):
    # Random row and column permutations
    random.shuffle(grid)
    transposed = [list(row) for row in zip(*grid)]
    random.shuffle(transposed)
    return transposed

def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        ascii_val = ord(char)
        row = (ascii_val // 10) % 9
        col = (ascii_val % 10) % 9
        encrypted_text += str(key[row][col])

    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for digit in encrypted_text:
        row, col = divmod(int(digit) - 1, 9)
        ascii_val = row * 10 + col
        decrypted_text += chr(ascii_val)

    return decrypted_text

# Example usage:
plaintext = "HELLO"
sudoku_key = generate_sudoku_grid()
permuted_key = apply_permutations(sudoku_key)

encrypted_text = encrypt(plaintext, permuted_key)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, permuted_key)
print("Decrypted:", decrypted_text)
