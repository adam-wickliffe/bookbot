def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def get_num_words(path_to_file):
    book_text = get_book_text(path_to_file)
    book_text = book_text.split()
    word_count = len(book_text)
    return word_count

def get_character_counts(path_to_file):
    book_text = get_book_text(path_to_file)
    book_text = book_text.lower()
    character_counts = {}
    for char in book_text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts