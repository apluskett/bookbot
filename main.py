from stats import word_count, letter_count
from sys import argv, exit

def get_book_text(book_name):
    try:
        with open(book_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{book_name}' not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_name = argv[1]
    book_text = get_book_text(book_name)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_name}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count(book_text)} total words')
    print('--------- Character Count -------')
    letter_counts = letter_count(book_text)
    for entry in letter_counts:
        print(f"{entry['char']}: {entry['num']}")
    print('============= END ===============')

main()