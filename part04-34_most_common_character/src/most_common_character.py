# Write your solution here
def most_common_character(name: str):
  quantity = []
  char = ""
  for i in name:
    if quantity == [] or name.count(i) > quantity:
      quantity = name.count(i)
      character = i
  return character


# Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

# An example of expected behaviour:

if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  # second_string = "exemplaryelementary"
  # print(most_common_character(second_string))

# Sample output

# b
# e