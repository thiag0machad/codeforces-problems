n = int(input())

for _ in range(n):
    word = input().strip()
    
    if len(word) > 10:
        print("{}{}{}".format(word[0], len(word) - 2, word[len(word) - 1]))
    else:
        print(word)