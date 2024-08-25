import matplotlib.pyplot as plt
from collections import Counter
from docx import Document

# Читання тексту з документа .docx
def get_text_from_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text.lower())
    return ' '.join(full_text)

# Обробка тексту та підрахунок частоти літер
def calculate_letter_frequency(text):
    # Український алфавіт
    alphabet = 'абвгґдеєжзийіклмнопрстуфхцчшщьюя'
    # Залишаємо лише букви українського алфавіту
    filtered_text = ''.join([char for char in text if char in alphabet])
    # Підрахунок частоти літер
    return Counter(filtered_text)

# Побудова гістограми
def plot_histogram(frequency):
    plt.figure(figsize=(10, 6))
    plt.bar(frequency.keys(), frequency.values(), color='blue')
    plt.xlabel('Літера')
    plt.ylabel('Частота')
    plt.title('Гістограма частоти появи літер у тексті')
    plt.show()

# Основна функція
def main():
    file_path = 'zacharovana-desna.docx'  # Шлях до вашого файлу
    text = get_text_from_docx(file_path)
    frequency = calculate_letter_frequency(text)
    plot_histogram(frequency)

if __name__ == '__main__':
    main()
