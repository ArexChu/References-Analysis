#coding:utf-8

import re
from collections import Counter
import matplotlib.pyplot as plt

words = []
shakes = open("CNKI-636575044865637500.txt", "r")

for line in shakes:
    if re.match("(.*)Keyword-关键词:(.*)", line):
        lines = line.split(":")[1]
        keywords = lines.split(";;")[-1]
        keyword = keywords.split(";")[-1]
        words.append(keyword)

#print(words)

counts = Counter(words).most_common(10)
#print(counts)

labels, values = zip(*counts)
print(labels)
print(values)

plt.bar(labels, values)
plt.show()
