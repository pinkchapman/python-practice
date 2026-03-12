def find_anomalous_words(text: str) -> list[str]:
    """
    Находит слова, длина которых отличается от средней длины слов в тексте более чем на 2 символа.

    

    :param text: Входная строка.
    :return: Список аномальных слов.
    """
    
    words = []

    for word in text.split():
        clean_word = word.strip(".,!?")
        if clean_word:
            words.append(clean_word)

    if not words:
        return []
    
    total = 0

    for word in words:
        total += len(word)

    avg_main = total / len(words)

    list_words = []

    for word in words:
        if abs(len(word) - avg_main) >= 2:
            list_words.append(word)

    return list_words
    
