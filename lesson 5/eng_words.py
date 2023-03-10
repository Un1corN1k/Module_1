import re


with open("text.txt", "r", encoding="utf-8") as file:
    l1 = file.read().split()
r = re.compile("[a-zA-Z]+")
eng_words = [w for w in filter(r.match, l1)]
print(f"Here are only english words: {eng_words}")
dictionary = {}
for i in eng_words:
    number = eng_words.count(i)
    dictionary[i] = number
dictionary = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
for x in dictionary:
    words, numbers = str(x).split(",")
    words = words[2:-1]
    numbers = numbers[:-1]
    print(f"The word '{words}' is reapeted {numbers}")
