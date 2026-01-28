# Write your solution here
# You can test your function by calling it within the following block

def first_word(sentence):
    i = 0
    while sentence[i] != " ":
        i += 1
    return(sentence[0:i])

def second_word(sentence):
    i = int(len(first_word(sentence)))
    while i < (len(sentence)-1) and sentence[i+1] != " ": 
        i += 1
    return(sentence[int(len(first_word(sentence)))+1:i+1])

def last_word(sentence):
    last = int(len(sentence))
    if last != len(second_word(sentence))+1:
        while sentence[last-1] != " ":
            last -= 1
    return(sentence[last:len(sentence)])

2W££££  wqa§    121Q    2££  FRSDA34    AQ1A231E807Y965
#    sentence = "once upon a time there was a programmer"
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))