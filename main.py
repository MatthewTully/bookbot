"""Code for Boot.dev Bookbot project."""


def count_words(string: str) -> int:
    """Count the words in a string."""
    split_str = string.split()
    return len(split_str)


def count_char(string: str) -> dict[str:int]:
    "Count the chars in string."
    lower_case_str = string.lower()
    result: dict[str,int] = {}
    for char in lower_case_str:
        if result.get(char, None) is None:
            result[char] = 1
        else:
            result[char] += 1
    return result

def get_book_as_string(book_path:str) -> str:
    """Open file and return string."""
    book_string = ""
    with open(book_path, "r", encoding="utf-8") as book:
        book_string = book.read()
        book.close()
    return book_string

def alpha_chars_only(char_dict: dict[str:int]) -> dict:
    """return new dict with only alpha chars."""
    new_dict = {}
    for char in char_dict:
        if char.isalpha():
            new_dict[char] = char_dict[char]
    return new_dict

def print_report(book_title: str, word_count: int, char_breakdown:list[dict]) -> None:
    print(f"--- Begin report of {book_title} ---\n")
    print(f"There are {word_count} in the book.\n\n")

    print("Alpha Character Breakdown - Occurance Hightest to lowest:\n")
    for item in char_breakdown:
        print(f"The character '{item['char']}' occurs {item['value']} times!")

    print("\n--- End Report ---")

def sort_on_value(dictionary: dict) -> int:
    """sort function."""
    return dictionary['value']

def char_dict_to_sorted_list(char_dict: dict, reverse:bool=False) -> list:
    """sorts dict."""

    list_dicts = []
    for char in char_dict:
        list_dicts.append({'char': char, 'value': char_dict[char]})
    list_dicts.sort(reverse=reverse, key=sort_on_value)
    return list_dicts

def main():
    book_path = "./books/frankenstein.txt"
    
    book = get_book_as_string(book_path)
    word_count = count_words(book)
    char_dict = count_char(book)
    alpha_dict = alpha_chars_only(char_dict)
    alpha_list = char_dict_to_sorted_list(alpha_dict, True)


    print_report(book_path, word_count, alpha_list)

main()