class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def back(first, path):
            if len(path) == k:
                res.append(path[:])
                return 

            for candidate in range(first, n + 1):
                path.append(candidate)
                back(candidate + 1, path)
                path.pop()

        back(1, [])
        return res