def convert(s, numRows):
    sLen = len(s)
    if sLen < 3:
        return s
    
    rows = [[] for _ in range(numRows)] # 5 rows
    if numRows == 1:
        return s
    elif numRows == 2:
        return s[::2] + s[1::2]
    
    currentRow = 0
    direction = 1
    for i in range(len(s)):
        rows[currentRow].append(s[i])
        currentRow += direction
        if currentRow == numRows-1: #hit bottom
            direction = -1

        if currentRow == 0 and i != 0: #hittop
            direction = 1
    result = []
    for row in rows:
        for char in row:
            result.append(char)
    return "".join(result)


    

print(convert("PAYPALISHIRING", 3))


#P              H
#A          S   I
#Y      I       R       
#P  L           I   G
#A              N
# PAYPALISHIRING