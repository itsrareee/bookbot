import sys
from stats import count_words
from stats import get_characters
from stats import start_sorting

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]     
    text = get_book_text(path_to_file)
    word_count = count_words(text)
    char_count = get_characters(text)
    sorting = start_sorting(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorting:
          print(f"{char['char']}: {char['num']}")

main()