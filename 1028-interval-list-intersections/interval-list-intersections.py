class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        pointer_1 = 0
        pointer_2 = 0         
        out = []
        while pointer_1 < len(firstList) and pointer_2 < len(secondList):
            a_start, a_end = firstList[pointer_1]
            b_start, b_end = secondList[pointer_2]
            if a_start <= b_end and b_start <= a_end:                       
                out.append([max(a_start, b_start), min(a_end, b_end)])   
                
            if a_end <= b_end:        
                pointer_1 += 1               
            else:                      
                pointer_2 += 1  
                 
        return out
