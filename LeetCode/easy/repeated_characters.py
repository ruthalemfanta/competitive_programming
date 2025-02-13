#iterate of the charcters and as soon as its equal to the seen break the iteration

def repeatedCharacters(s_):
        seen = set()
        for char in s:
            if char in seen:
                return char  
            seen.add(char)
        return None  



s = "nwcn"
print(repeatedCharacters(s))