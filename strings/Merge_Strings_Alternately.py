def mergeAlternately(word1: str, word2: str):
    ans = []
    for i in range(min(len(word1), len(word2))):
        ans.append(word1[i])
        ans.append(word2[i])
        print(ans)
    if len(word1) > len(word2):
        ans.append(word1[i+1::])
        return "".join(ans)
    elif len(word1) < len(word2):
        ans.append(word2[i+1::])
        return "".join(ans)
    return "".join(ans)

print(mergeAlternately("ab","pqrs"))