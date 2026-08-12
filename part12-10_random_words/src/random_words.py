# Write your solution here:
import random


def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        yield ''.join(random.choice(characters) for _ in range(length))



    # random_words = []
    # while len(random_words) < amount:
    #     random_words.append(random.choice(characters) * length)

    # yield random_words


if __name__ == "__main__":

    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)