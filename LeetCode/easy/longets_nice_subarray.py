def longetsSubString(s):
    def is_nice(sub):
        return all(c.lower() in sub and c.upper() in sub for c in sub)
    
    n = len(s)
    longest_nice_sub = ""
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_nice(substring):
                if len(substring) > len(longest_nice_sub):
                    longest_nice_sub = substring

    return longest_nice_sub if longest_nice_sub else''


