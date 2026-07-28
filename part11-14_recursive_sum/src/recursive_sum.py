# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    if number <= 1:
        return number
    sum = 0
    sum += number
    number -= 1
    if number == 1:
        return sum + 1
    else:
        recursive_sum(number)



result = recursive_sum(3)
print(result)

print(recursive_sum(5))
print(recursive_sum(10))