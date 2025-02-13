def removeDuplicates(string):
    new = []
    for char in string:
        if new and char == new[-1]:
            new.pop()
        else:
            new.append(char)
    return ''.join(new)



string = "abbaca"  
print(removeDuplicates(string)) # ['c', 'a']


    



