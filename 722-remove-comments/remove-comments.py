class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        strr = "\n".join(source)
        result = ""

        i = 0
        while i < len(strr):

            two = strr[i:i+2]
            if two == "//":

                i += 2
                while i < len(strr) and strr[i] != "\n":
                    i += 1

            elif two == "/*":

                i += 2
                while strr[i:i+2] != "*/":
                    i += 1
                i += 2

            else:
                result += strr[i]
                i += 1

        
        ans = []

        for line in result.split("\n"):
            if line != "":
                ans.append(line)


        return ans        