def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] = char_counts[char.lower()] + 1
        else:
            char_counts[char.lower()] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def letter_counts(char_counts):
    letters = []
    for key, value in char_counts.items():
        if key.isalpha():
            letters.append({"name": key, "num": value})
    letters.sort(reverse=True, key=sort_on)
    return letters

def build_report(book, word_count, letters):
    report = f"--- Begin report of {book} ---\n"
    report += f"{word_count} words found in the document\n\n"
    for dict in letters:
        key = dict["name"]
        value = dict["num"]
        report += f"The '{key}' character was found {value} times\n"
    report += "--- End report ---"
    return report

def main():
    book = "books/frakenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    #print(file_contents)
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    letter_count = letter_counts(char_count)
    print(build_report(book, word_count, letter_count))



main()