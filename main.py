def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(count(file_contents))
    
def count(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    main()