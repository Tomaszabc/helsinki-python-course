# Write your solution here
def no_shouting(my_list: list):
  new_list = []
  for string in my_list:
    if not string.isupper():
      new_list.append(string)
  return new_list


# The Python string method isupper() returns True if a string consists of only uppercase characters.

# Some examples:

# print("XYZ".isupper())

# is_it_upper = "Abc".isupper()
# print(is_it_upper)

# Sample output

# True
# False

# Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

# An example of expected behaviour:
if __name__ == "__main__":
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)

# Sample output

# ['def', 'lower', 'another lower', 'Capitalized']