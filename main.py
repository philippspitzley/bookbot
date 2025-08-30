import sys

from stats import get_char_count, get_num_words, print_stats, sort_char_count

# check args
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]


def get_book_text(path: str) -> str:
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)


def main():
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    char_counts = get_char_count(book_text)
    sorted_char_counts = sort_char_count(char_counts)

    print_stats(num_words=num_words, char_counts=sorted_char_counts)


if __name__ == "__main__":
    main()
