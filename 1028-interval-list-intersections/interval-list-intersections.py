class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        pointer_1 = 0
        pointer_2 = 0         
        out = []
        while pointer_1 < len(firstList) and pointer_2 < len(secondList):
            first_start, first_end = firstList[pointer_1]
            second_start, second_end = secondList[pointer_2]
            if first_start <= second_end and second_start <= first_end:                       
                out.append([max(first_start, second_start), min(first_end, second_end)])   
                
            if first_end <= second_end:        
                pointer_1 += 1               
            else:                      
                pointer_2 += 1  
                 
        return out
