def main():
    # file_contents = read("books/frankenstein.txt")
    # print(file_contents)
    # print(countWords(file_contents))
    # print(countCharacters(file_contents))
    report("books/frankenstein.txt")

def read(path):
    with open(path) as f:
        return f.read()
    
def countWords(text):
    words = text.split()
    return len(words)

def countCharacters(text):
    characters = {}
    for t in text:
        character = t.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

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
        print(f"The '{item["letter"]}' character was found {item["occurence"]} times")

    print("--- End report ---")

if __name__ == '__main__':
    main()
