class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift_arr = [0] * (n + 1)

        for shift in shifts:
            start, end, direction = shift
            shift_arr[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                shift_arr[end + 1] -= (1 if direction == 1 else -1)

        cur_shift = 0
        shift_l = list(s)
        for i in range(n):
            cur_shift += shift_arr[i]
            netShift = (cur_shift % 26 + 26) % 26
            shift_l[i] = chr((ord(shift_l[i]) - ord('a') + netShift) % 26 + ord('a'))

        return ''.join(shift_l)