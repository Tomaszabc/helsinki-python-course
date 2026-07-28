# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as file:
        content = file.read()

    words = content.split()
    clean_words = [word.strip(".,!?;:()\"'") for word in words]

    counts = {}
    for word in clean_words:
        counts[word] = counts.get(word, 0) + 1

    result = {}
    return {word: count for word, count in counts.items() if count >= lower_limit}

# print(most_common_words("comprehensions.txt", 3))