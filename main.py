from stats import countWords, countCharacters

import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    report(sys.argv[1])

def read(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["occurence"]

def report(path):
    text = read(path)
    count = countWords(text)
    dictionary = countCharacters(text)

    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")

    list_dict = []
    for letter in dictionary:
        if letter.isalpha():
            occurence = dictionary[letter]
            list_dict.append({"letter": letter, "occurence": occurence})

    list_dict.sort(reverse=True, key=sort_on)
    
    for item in list_dict:
        print(f"{item["letter"]}: {item["occurence"]}")

    print("--- End report ---")

if __name__ == '__main__':
    main()
