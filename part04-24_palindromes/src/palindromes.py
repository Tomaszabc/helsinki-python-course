# Write your solution here

def palindromes(word: str):
  word = list(word)
  palindrome =[]
  for i in range(len(word)-1, -1, -1):
    palindrome.append(word[i])
  return word == palindrome

word = input("Please type in a palindrome: ")
ara432    print("that wasn't a palindrome")
    word = input("Please type in a palindrome: ")

print(word, "is a palindrome!")

 
# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.

# Please also write a main program which asks the user to type in words until they type in a palindrome:
# Sample output

# Please type in a palindrome: python
# that wasn't a palindrome
# Please type in a palindrome: java
# that wasn't a palindrome
# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
#   print(palindromes("qqqq"))
