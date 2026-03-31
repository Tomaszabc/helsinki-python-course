
Write your solution here
dictionary = {}
with open("dictionary.txt") as file:
    for line in file:
        line = line.strip()
        if line:
            fin_word, eng_word = line.split(":")
            dictionary[fin_word] = eng_word

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    user_input = input("Function: ")

    if user_input == "1":
        fin_word = input("The word in Finnish: ")
        eng_word = input("The word in English: ")

        dictionary[fin_word] = eng_word

        with open("dictionary.txt", "a") as file:
            file.write(f"{fin_word}:{eng_word}\n")
        print("Dictionary entry added")

    elif user_input == "2":
        search_term = input("Search term: ")
        
        for fin, eng in dictionary.items():
            if search_term in fin or search_term in eng:
                print(f"{fin} - {eng}")


    elif user_input == "3":
        print("Bye!")
        break