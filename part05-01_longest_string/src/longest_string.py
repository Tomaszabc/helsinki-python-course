def longest(strings: list):
    longest = ""
    for item in strings:
        if len(item) > len(longest):
            longest = item
    return longest

if __name__ == "__main__":
    strings = ['ab', 'abcd', 'abc', 'acbdefg', 'a', 'abcd', 'aa']
    print(longest(strings))

