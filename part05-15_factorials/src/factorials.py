# Write your solution here
def factorials(n: int):
    f = {}
    for i in range(n, 0, -1):
        f[i] = i
        for j in range(i, 1, -1):
            f[i] *= (j-1)
    
    return f



if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[2])
    print(k[3])
    print(k[4])
    print(k[5])


# def factorials(n: int):
#     f = {}
#     f[5] = 5
#     for i in range(1, 5):
        
#         f[5] *= 5-i
    
#     return f