
def stringCompression(s):
    result = []
    count = 0
    for i in s:
        count = s.count(i)
        if i not in result:
             if count == 1:
                result.append(i)
             else:
                result.append(i)
                result.append(str(count)) 

    return len(result)

s = ["a","a","b","b","c","c","c"]
print(test(s)) # 6