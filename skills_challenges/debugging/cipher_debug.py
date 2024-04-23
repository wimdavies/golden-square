def encode(text, key):
    print("Encode has been called")
    cipher = make_cipher(key)
    print(f"Cipher from make_cipher in encode is:\n{cipher}")

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    print("Decode has been called")
    cipher = make_cipher(key)
    print(f"Cipher from make_cipher is {cipher}")

    plaintext_chars = []
    for i in encrypted:
        # Fixed: cipher index operands were the wrong way around
        plain_char = cipher[ord(i) - 65]
        print(f"encrypted_char is {i}. plain_char is {plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    print("make_cipher has been called")

    # Fixed: chr() was for wrong integer, and range did not include 'z'
    alphabet = [chr(i + 96) for i in range(1, 27)]
    print(f"Alphabet in make_cipher is:\n{alphabet}")
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

