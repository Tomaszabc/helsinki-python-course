# Write your solution here
import random

def words(n: int, beginning: str):
    word_list = []

    with open("words.txt") as file:
        for line in file:
            word = line.strip()
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError(f"Not enough words beginning with '{beginning}'")
    return random.sample(word_list, n)