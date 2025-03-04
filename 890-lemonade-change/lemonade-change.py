class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5:
            return False
        
        fiv = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                fiv += 1
            elif bill == 10:
                if fiv > 0:
                    fiv -= 1
                else:
                    return False
                ten += 1
            else:
                if fiv > 0 and ten > 0:
                    fiv -= 1
                    ten -= 1
                elif fiv > 2 :
                    fiv -= 3
                else:
                    return False
        return True