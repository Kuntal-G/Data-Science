# Checking whether a string is anagram of another

# Approach-1 (Python Counter)

from collections import Counter


def checkAnagram1(str1, str2):
    return (Counter(str1) == Counter(str2))


print(checkAnagram1("listen", "silent"))


# Approach-2 (Using sorted)

def checkAnagram2(str1, str2):
    return (sorted(str1) == sorted(str2))


print(checkAnagram2("listen", "silents"))
