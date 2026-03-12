def read_dictionary():
    dictionary = []

    with open("dictionary.txt") as file:
        for row in file:
            row = row.replace("\n","")
            dictionary.append(tuple(row.split(";")))

    return dictionary

def add_word(dictionary: list):
    word_fi = input("The word in Finnish: ")
    word_en = input("The word in English: ")

    dictionary.append((word_fi, word_en))

    with open("dictionary.txt", "a") as file:
        file.write(word_fi + ";" + word_en + "\n")
        print("Dictionary entry added")

def search_word(dictionary: list):
    word = input("Search term: ")
    for word_fi, word_en in dictionary:
        if word in word_fi or word in word_en:
            print(f"{word_fi} - {word_en}")

dictionary = read_dictionary()
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        add_word(dictionary)
    elif function == "2":
        search_word(dictionary)
    elif function == "3":
        print("Bye!")
        break


# Write your solution here
# dictionary = {}
# with open("dictionary.txt") as file:
#     for line in file:
#         line = line.strip()
#         if line:
#             fin_word, eng_word = line.split(":")
#             dictionary[fin_word] = eng_word

# while True:
#     print("1 - Add word, 2 - Search, 3 - Quit")
#     user_input = input("Function: ")

#     if user_input == "1":
#         fin_word = input("The word in Finnish: ")
#         eng_word = input("The word in English: ")

#         dictionary[fin_word] = eng_word

#         with open("dictionary.txt", "a") as file:
#             file.write(f"{fin_word}:{eng_word}\n")
#         print("Dictionary entry added")

#     elif user_input == "2":
#         search_term = input("Search term: ")
        
#         for fin, eng in dictionary.items():
#             if search_term in fin or search_term in eng:
#                 print(f"{fin} - {eng}")


#     elif user_input == "3":
#         print("Bye!")
#         break