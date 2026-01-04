import sys
from stats import get_num_words, get_character_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    word_count = get_num_words(path_to_file)
    character_counts = get_character_counts(path_to_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    #print(character_counts)
    character_counts = dict(sorted(character_counts.items()))
    for char, count in character_counts.items():
        print(f"{char}: {count}")

main()
