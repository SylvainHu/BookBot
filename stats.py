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