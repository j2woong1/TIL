def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for vowel in vowels:
        count += word.count(vowel)
    return count

print(count_vowels('apple'))
print(count_vowels('banana'))