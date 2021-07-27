def low_and_up(word):
    new = ''
    for i in range(len(word)):
        if not i % 2:
            new += word[i]
        else:
            new += word[i].upper()

    return new


print(low_and_up('apple'))
print(low_and_up('banana'))