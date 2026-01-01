from stats import get_num_words, get_count_of_each_char, sort_occurances
import books
import sys

def main():
    entries = sys.argv
    if len(entries) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    num_words = get_num_words(path)
    occur_of_chars = get_count_of_each_char(path)
    sorted_dict = sort_occurances(occur_of_chars)
    printing_sorted_dict = ''
    for k,v in sorted_dict.items():
        printing_sorted_dict += f'{k}: {v}\n'
    print(f'============ BOOKBOT ============\n Analyzing book found at {path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------\n{printing_sorted_dict}\n============= END ===============')

main()