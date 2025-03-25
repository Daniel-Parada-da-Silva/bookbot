import sys
from stats import get_num_words
from stats import count_characters

def sort_on(dic):
    return dic["times"]

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def create_list(dic):
    lis = []
    for entry in dic:
        if entry.isalpha():
            element = {"char": entry, "times": dic[entry]}
            lis.append(element)
    lis.sort(reverse=True,key=sort_on)
    return lis

def format(path, words, dic):
    lis = create_list(dic)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print(f"----------- Word Count ----------")
    print(f"Found {words} total words")
    print(f"")
    for entry in lis:
        print(f"{entry["char"]}: {entry["times"]}")
    print(f"============= END ===============")

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]
    contents = get_book_text(path)
    words = get_num_words(contents)
    dict = count_characters(contents)
    format(path, words, dict)

main()