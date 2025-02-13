class myArray:
    def __init__(self) -> None:
        self.length = 0
        self.data = {}

    def get(self, index):
        if self.length == 0:
            return 'empty array'
        elif index < 0 or index >= self.length:
            return 'out of bound'
        else:
            return self.data[index]
        
    def push(self, ele):
        self.data[self.length] = ele
        self.length += 1
        return self.data
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem
    
    def delete(self, index): 
        deleted = self.data[index]
        self.shiftItems(index)
        return deleted

    def shiftItems(self, index):
        i = index
        while i < self.length-1:
            self.data[i] = self.data[i+1]
            i += 1
        self.data[self.length-1]



        
    


newArray = myArray()
print(newArray.push(10))
print(newArray.get(10))
print(newArray.push(2))
print(newArray.push(15))
print(newArray.delete(1))
print(newArray.push(15))




