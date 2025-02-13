def backSpaceCompare(s, t):
    def backSpace(string):
        new = []
        for char in string:
            if char == "#" and new:
                new.pop() 
            elif char != "#":
                new.append(char) 
        return ''.join(new)  
    
    return backSpace(s) == backSpace(t)


s = "y#fo##f"
t = "y#f#o##f"
print(backSpaceCompare(s, t)) 
