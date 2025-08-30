def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict[str, int]:
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_char_count(char_count: dict[str, int]) -> list[dict[str, int]]:
    chars = []

    for char, count in char_count.items():
        chars.append({"char": char, "count": count})

    return sorted(chars, key=lambda x: x["count"], reverse=True)


def print_stats(num_words: int, char_counts: list[dict[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in char_counts:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
