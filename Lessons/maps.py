# Practice with maps
from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# Three ways of getting the same output.
# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# print(list(map(jumble,words)))

print([jumble(word) for word in words])
