def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_letter_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print (f"- Report of: {book_path} -\n")
    print (f"{num_words} words found in this document\n")
    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("\n- End report -")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(file):
    words = file.split()
    return len(words)

def get_letter_count(file):
    letters = {}
    for c in file:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        if not ch.isalpha():
            continue
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()