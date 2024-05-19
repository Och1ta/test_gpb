def load_words(filename):
    """
    Загружает слова из текстового файла и возвращает их в виде списка.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words


def create_combined_words(first_word, words):
    """
    Создает список новых слов путем сцепления первого слова с каждым словом из списка.
    """
    combined_words = [first_word + word for word in words]
    return combined_words


def main():
    # Имя текстового файла с набором слов
    filename = '5_test.txt'

    # Загрузка слов из файла
    words = load_words(filename)

    # Запрос первого слова у пользователя
    first_word = input("Введите первое слово: ")

    # Создание новых слов путем сцепления
    combined_words = create_combined_words(first_word, words)

    # Вывод результатов
    for word in combined_words:
        print(word)


if __name__ == "__main__":
    main()
