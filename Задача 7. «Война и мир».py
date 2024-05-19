def calculate_frequency(text):
    stats = {}
    total_chars = 0
    for char in text:
        if char.isalpha() or char == " ":
            if char.lower() in stats:
                stats[char.lower()] += 1
            else:
                stats[char.lower()] = 1
            total_chars += 1

    frequency = {char: count / total_chars for char, count in stats.items()}

    return frequency


def find_name_variations(name):
    name_variations = [name.lower(), name.lower()[:-1] + "ю", name.lower()[:-1] + "я"]
    return name_variations


def find_sentences_with_name(text, name):
    sentences = text.split(". ")
    name_sentences = []
    name_variations = find_name_variations(name)
    for sentence in sentences:
        for variation in name_variations:
            if variation in sentence.lower():
                name_sentences.append(sentence + ".")
                break
        if len(name_sentences) == 10:
            break

    return name_sentences


# Чтение файла
with open("war_and_peace.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Вычисление статистики по буквам и символам
frequency = calculate_frequency(text)
for char, freq in frequency.items():
    print(f"{char} : {freq:.2f}")

# Поиск предложений с именем Андрей
name = "Андрей"
name_sentences = find_sentences_with_name(text, name)
print("\nПредложения со словом «Андрей»:")
for sentence in name_sentences:
    print(sentence)