def reverseWords(s):
    words = s.split()
    words.reverse()
    print(words)
    return " ".join(words)

print(reverseWords("the thing  is "))