# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    # filtered_chars = [char for char in string if char not in forbidden]
    # return "".join(filtered_chars)
    string_split = [char for char in string]
    return "".join([char for char in string_split if char not in forbidden])


sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)