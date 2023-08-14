def check_string_contains_three_vowels(string: str) -> bool:
    pass


def check_letter_appears_twice(string: str) -> bool:
    pass


def check_does_not_contain_key_pairs(string: str) -> bool:
    pass


def open_file():
    with open('five_file.txt', 'r') as obj_file:
        file = obj_file.read()
    return file


if __name__ == "__main__":
    good_strings = []
    file = open_file()
    for string in file:
        print(file)
        # check if all 3 pass here and add to list
