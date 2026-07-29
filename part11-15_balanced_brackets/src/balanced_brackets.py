
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    
    if not my_string[0] in "()[]":
        return balanced_brackets(my_string[1:])

    if not my_string[-1] in "()[]":
        return balanced_brackets(my_string[:-1])

    if my_string[0] == "(" and my_string[-1] == ")":
        return balanced_brackets(my_string[1:-1])
    if my_string[0] == "[" and my_string[-1] == "]":
            return balanced_brackets(my_string[1:-1])

    return False



    # my_string_clean = [char for char in my_string if char in "()[]"]
    
    # if len(my_string_clean) == 0:
    #     return True

    # first = my_string_clean[0]
    # last = my_string_clean[-1]

    # if (first == '(' and last == ')') or (first == '[' and last == ']'):
    #     remaining = my_string_clean[1:-1]
    #     return balanced_brackets("".join(remaining))
    # else:
    #     return False

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)