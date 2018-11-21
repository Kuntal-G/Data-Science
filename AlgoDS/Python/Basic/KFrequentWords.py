#Print K most frequent words in a string

from collections import Counter
def kFreqWords(str,k):

    str=str.split(" ")

    count=Counter(str)

    return count.most_common(k)

input="Welcome to the world of Geeks This portal has been created to provide well written well thought and well explained solutions for selected questions"

print(kFreqWords(input,4))
