def vigenere_encrypt(plaintext, key):
    alphabet = 'абвгґдеєжзийіклмнопрстуфхцчшщьюя'
    encrypted_text = []
    key_repeated = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]

    for p, k in zip(plaintext, key_repeated):
        if p in alphabet:
            p_index = alphabet.index(p)
            k_index = alphabet.index(k)
            encrypted_char = alphabet[(p_index + k_index) % len(alphabet)]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(p)  # Додаємо неалфавітні символи без змін

    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, key):
    alphabet = 'абвгґдеєжзийіклмнопрстуфхцчшщьюя'
    decrypted_text = []
    key_repeated = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]

    for c, k in zip(ciphertext, key_repeated):
        if c in alphabet:
            c_index = alphabet.index(c)
            k_index = alphabet.index(k)
            decrypted_char = alphabet[(c_index - k_index) % len(alphabet)]
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(c)  # Додаємо неалфавітні символи без змін

    return ''.join(decrypted_text)


# Приклад використання:
plaintext = "це тестовий текст"
key = "ключ"

encrypted = vigenere_encrypt(plaintext, key)
print(f"Зашифрований текст: {encrypted}")

decrypted = vigenere_decrypt(encrypted, key)
print(f"Розшифрований текст: {decrypted}")
