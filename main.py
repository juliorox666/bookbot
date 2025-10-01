from stats import get_word_count, get_letter_count, sort_on_value
import sys


def get_book_text(book_path):
    with open(book_path, "r") as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    # print(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing {book_path}...")
    print("----------- Word Count ----------")
    get_word_count(text)
    print("--------- Character Count -------")
    # print(get_letter_count(text))
    
    for item in sort_on_value(get_letter_count(text)):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============ END ============")

if __name__ == "__main__":
    main()


