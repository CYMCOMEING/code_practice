import sys
import string

files = ['ping子网.py',]
words = {} 
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in files:
    for line in open(filename):
        for word in line.split():
            word = word.strip(strip)
            if len(word) >= 2:
                words[word] = words.get(word, 0) + 1

for word in sorted(words):
    print("'{0}' occurs {1} times".format(word,words[word]))
