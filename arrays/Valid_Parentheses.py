def isValid(s: str) -> bool:
        openers = set("([{")
        closers = set(")]}")
        pairs = {")":"(", "]":"[", "}":"{"}
        open = []

        for bracket in s:
            if bracket in openers:
                open.append(bracket)
                continue
            if bracket in closers:
                if not open:
                     return False 
                if pairs[bracket] != open.pop():
                    return False
        return not open
            
print(isValid("()"))

               