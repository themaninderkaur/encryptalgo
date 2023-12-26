# Sudoku Encryption Library

The ealgo library is an amaetuer Python module that provides functions for encrypting and decrypting messages using a simple form of Sudoku-based encryption. It includes a random number generator and functions for generating Sudoku grids, applying permutations, and performing encryption and decryption.

## Installation

To use the Sudoku Encryption Library, follow these steps:

1. Download the `sudoku_encryption.py` file.
2. Place the file in your project directory.

## Usage

### Importing the Library

```python
from sudoku_encryption import SimpleRandom, generate_sudoku_grid, apply_permutations, encrypt, decrypt
```

### Generating a Sudoku Key

```python
seed_value = 42
random_generator = SimpleRandom(seed_value)

sudoku_key = generate_sudoku_grid()
permuted_key = apply_permutations(sudoku_key, random_generator)
```

### Encrypting and Decrypting

```python
plaintext = "HELLO"

encrypted_text = encrypt(plaintext, permuted_key, random_generator)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, permuted_key, random_generator)
print("Decrypted:", decrypted_text)
```

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This Sudoku Encryption Library is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

