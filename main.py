from stats import get_num_words, group_by_character
import sys

def get_book_text(filePath): 
    with open(filePath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(get_num_words(get_book_text(filepath)))
    print("--------- Character Count -------")
    
    
    for value in group_by_character(get_book_text(filepath)):
        if value[0].isalpha():
            print(f"{value[0]}: {value[1]}")
    
    print("============= END ===============")
main()
    