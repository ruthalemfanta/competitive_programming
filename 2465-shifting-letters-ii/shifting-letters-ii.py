class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        shift_arr = [0] * (len(s) + 1)

        for left, right, direction in shifts:  
            shift_arr[left] += (1 if direction == 1 else -1) 

            if right + 1 < len(s):
                shift_arr[right + 1] -= (1 if direction == 1 else -1)
        prefix = []
        acc = 0

        for i in shift_arr:
            acc += i
            prefix.append(acc)

        result = []
        for i in range(len(s)):
            result.append(chr((ord(s[i]) - ord('a') + (prefix[i] % 26 + 26) % 26) % 26 + ord('a')))

        return ''.join(result) 


