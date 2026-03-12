# write your solution here
if True:
    user_text = input("Write some text")
else:
    user_text = "We use ptython to make a spell checker"

wordlist = "wordlist.txt"

correct_words = []
with open(wordlist) as file:
    for line in file:
        word = line.strip()
        correct_words.append(word.lower())

words = user_text.split(" ")

final_parts = []
for i in range(len(words)):
    if words[i].lower() in correct_words:
        final_parts.append(words[i])
    else:
        final_parts.append(f"*{words[i]}*")
final_string = " ".join(final_parts)
print(final_string)

