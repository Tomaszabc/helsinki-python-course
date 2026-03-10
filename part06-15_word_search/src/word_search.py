

def find_words(search_term: str):
    words_stripped = []
    with open("words.txt") as file:
        for line in file:
            words_stripped.append(line.strip())
    
    words_found = []

    if search_term.startswith("*"):
        suffix = search_term[1:]

        for word in words_stripped:
            if word.endswith(suffix):
                words_found.append(word)

    elif search_term.endswith("*"):
        prefix = search_term[:-1]

        for word in words_stripped:
            if word.startswith(prefix):
                words_found.append(word)

    elif "." in search_term:
        for word in words_stripped:
            if len(word) != len(search_term):
                continue

            match = True
            for i in range(len(search_term)):
                if search_term[i] != "." and search_term[i] != word[i]:
                    match = False
                    break
            if match:
                words_found.append(word)
    else:
        for word in words_stripped:
            if word == search_term:
                words_found.append(word)

    return(words_found)
