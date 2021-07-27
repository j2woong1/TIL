def duplicated_letters(word):
    duplicates = []

    for c in word:
        if (word.count(c) > 1) and (c not in duplicates):
            duplicates.append(c)

    return duplicates


print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
