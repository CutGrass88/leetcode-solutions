def gcdOfStrings(str1: str, str2: str):
    for size in range(min(len(str1), len(str2)),0 ,-1):
        if len(str1) % size != 0 or len(str2) % size != 0:
            continue
        prefix = str1[:size]
        if prefix * (len(str1) // size) == str1 and prefix * (len(str2) // size) == str2:
            return prefix
    return ""



print(gcdOfStrings("ABABAB","ABAB"))