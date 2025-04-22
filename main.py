from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path = sys.argv[1]
    
    try:
        book = read_book(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)

    word_count = count_words(book)
    char = char_count(book)
    sorted_list = sort_dict(char)
    print ("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count -----")

    for letter, count in sorted_list:
        if letter.isalpha():
            print(f"{letter}: {count}")


if __name__ == "__main__":
    main()