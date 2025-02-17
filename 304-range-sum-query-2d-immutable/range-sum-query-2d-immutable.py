class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.summ = []
        for i in range(rows + 1):
            row = []
            for j in range(cols + 1):
                row.append(0)
            self.summ.append(row)
        for row in range(len(self.summ)-1):
            for col in range(len(self.summ[0])-1):
                self.summ[row+1][col+1]=matrix[row][col] + self.summ[row][col+1] + self.summ[row+1][col] - self.summ[row][col]

        print(self.summ)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.summ[row2+1][col2+1] - self.summ[row1][col2+1] - self.summ[row2+1][col1] + self.summ[row1][col1]
                            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)