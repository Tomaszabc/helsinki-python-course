import difflib

def wordlist():
    words = []
    with open("wordlist.txt") as file:
        for rivi in file:
            words.append(rivi.strip())
    return words

words = wordlist()
sentence = input("write text: ")
error = []
for word in sentence.split(' '):
    if word.lower() in words:
        print(word+ " ", end="")
    else:
        error.append(word)
        print("*" + word+ "* ", end="")
print()

print("suggestions:")
for word in error:
    suggestion_list = difflib.get_close_matches(word, words)
    suggestions = ", ".join(suggestion_list)
    print(f"{word}: {suggestions}")

# # write your solution here
# from difflib import get_close_matches

# if True:
#     user_text = input("Write text: ")
# else:
#     user_text = "We use ptython to make a spell checker"

# wordlist = "wordlist.txt"

# # Wczytaj poprawne słowa do listy
# correct_words = []
# with open(wordlist) as file:
#     for line in file:
#         word = line.strip()
#         correct_words.append(word.lower())

# # Podziel tekst na słowa
# words = user_text.split()

# # Znajdź błędne słowa i zaproponuj sugestie
# final_parts = []
# misspelled = {}  # słownik: błędne słowo -> lista sugestii

# for word in words:
#     # Usuń znaki interpunkcyjne dla sprawdzenia
#     clean_word = word.strip(".,!?;:()\"'")
    
#     if clean_word.lower() in correct_words:
#         final_parts.append(word)  # poprawne słowo - bez gwiazdek
#     else:
#         final_parts.append(f"*{word}*")  # błędne słowo - z gwiazdkami
        
#         # Znajdź sugestie tylko dla oryginalnego słowa (bez interpunkcji)
#         if clean_word.lower() not in misspelled:
#             suggestions = get_close_matches(clean_word.lower(), correct_words, n=3, cutoff=0.6)
#             if suggestions:
#                 misspelled[clean_word.lower()] = suggestions

# # Wydrukuj poprawiony tekst
# print(" ".join(final_parts))

# # Wydrukuj sugestie
# if misspelled:
#     print("suggestions:")
#     for wrong_word, suggestions in misspelled.items():
#         # Znajdź oryginalne słowo z interpunkcją (dla wyświetlenia)
#         original_word = None
#         for word in words:
#             if word.strip(".,!?;:()\"'").lower() == wrong_word:
#                 original_word = word
#                 break
        
#         # Wyświetl sugestie
#         suggestion_str = ", ".join(suggestions)
#         print(f"{original_word}: {suggestion_str}")