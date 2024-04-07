word = input()
while True:
    word2 = input()
    if word[-1] != word2[0]:
        print(word2)
        break
    word = word2