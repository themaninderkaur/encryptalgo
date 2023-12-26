from random_generator import SimpleRandom
from sudoku_encryption import generate_sudoku_grid, apply_permutations, encrypt, decrypt

def main():
    seed_value = 42
    random_generator = SimpleRandom(seed_value)

    plaintext = "HELLO"
    sudoku_key = generate_sudoku_grid()
    permuted_key = apply_permutations(sudoku_key, random_generator)

    encrypted_text = encrypt(plaintext, permuted_key, random_generator)
    print("Encrypted:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, permuted_key, random_generator)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
