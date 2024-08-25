import collections
import itertools
import string

# Визначаємо український алфавіт
alphabet = 'абвгґдеєжзийіклмнопрстуфхцчшщьюя'


# Функція для знаходження частоти появи кожної літери
def calculate_frequency(text):
    frequency = collections.Counter(text)
    total_chars = sum(frequency.values())
    return {char: freq / total_chars for char, freq in frequency.items()}


# Функція для шифрування за допомогою шифру Віженера
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_repeated = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]

    for p, k in zip(plaintext, key_repeated):
        if p in alphabet:
            p_index = alphabet.index(p)
            k_index = alphabet.index(k)
            encrypted_char = alphabet[(p_index + k_index) % len(alphabet)]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(p)

    return ''.join(encrypted_text)


# Функція для дешифрування за допомогою шифру Віженера
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_repeated = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]

    for c, k in zip(ciphertext, key_repeated):
        if c in alphabet:
            c_index = alphabet.index(c)
            k_index = alphabet.index(k)
            decrypted_char = alphabet[(c_index - k_index) % len(alphabet)]
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(c)

    return ''.join(decrypted_text)


# Функція для оцінки ключової довжини (використовуючи метод Касіскі та інші методи)
def kasiski_examination(ciphertext, max_key_length=20):
    distances = []
    for length in range(3, 6):  # Ми шукаємо повторення підрядків довжиною 3-5 символів
        for i in range(len(ciphertext) - length):
            sub = ciphertext[i:i + length]
            for j in range(i + length, len(ciphertext) - length):
                if ciphertext[j:j + length] == sub:
                    distances.append(j - i)

    factors = collections.Counter()
    for dist in distances:
        for i in range(2, max_key_length + 1):
            if dist % i == 0:
                factors[i] += 1

    return factors.most_common(1)[0][0] if factors else 1


# Функція для частотного аналізу та криптоаналізу
def frequency_analysis(ciphertext, key_length):
    key = ''
    for i in range(key_length):
        segment = ciphertext[i::key_length]
        freq = calculate_frequency(segment)
        most_common_char = max(freq, key=freq.get)
        # Зсув найчастішої літери відносно 'о' (найчастіша літера в українській мові)
        shift = (alphabet.index(most_common_char) - alphabet.index('о')) % len(alphabet)
        key += alphabet[shift]
    return key


# Функція для криптоаналізу шифру Віженера
def vigenere_cryptanalysis(ciphertext):
    key_length = kasiski_examination(ciphertext)
    estimated_key = frequency_analysis(ciphertext, key_length)
    decrypted_text = vigenere_decrypt(ciphertext, estimated_key)
    return estimated_key, decrypted_text


# Приклад використання
ciphertext = "шзгшфоьхяикйофяшидопгоффгжцдшозшпьофзшфждчщйцоьжцшцсжфоюьоцшфгщшщфоузйояц"  # Ваш зашифрований текст

key, decrypted_text = vigenere_cryptanalysis(ciphertext)

print(f"Оцінений ключ: {key}")
print(f"Розшифрований текст: {decrypted_text}")
