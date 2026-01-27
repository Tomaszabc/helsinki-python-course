# Write your solution here
def no_vowels(string: str):
  vowels = "aioue"
  new_string = ""

  for i in string.lower():
    if i not in vowels:
      new_string += i
  return new_string

# Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

# You can assume the string will contain only characters from the lowercase English alphabet a...z.

# An example of expected behaviour:

if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))

# Sample output

# ths s n xmpl