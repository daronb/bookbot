from stats import get_word_count, count_characters, list_of_dicts
import sys

def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()

def main():

    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    character_counts = count_characters(text)
    num_words = get_word_count(text)
    char_list = list_of_dicts(character_counts)
    # print(f"{num_words} words found in the document")
    # print(character_counts)
    # print(list_of_dicts(character_counts))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for char in char_list:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()