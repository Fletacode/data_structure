class Set():
    def __init__(self):
        self.arr = []
    
    def insertElement(self,data):
        # if len(self.arr) == 0:
        #     self.arr.append(data)
        #     return

        i = 0
        while i < len(self.arr) and data > self.arr[i]:
            i += 1
        
        if len(self.arr) == i:
            self.arr.append(data)
        else:
            self.arr.insert(i,data)
    
    def intersect(self, A ,B):
        temp = []
        i = 0
        j = 0
        while i < len(A.arr) and j < len(B.arr):
            if A.arr[i] < B.arr[j]:∑
                temp.append(A.arr[i])
                i += 1
            elif B.arr[j] < A.arr[i]:
                temp.apppend(B.arr[j])
                j += li
            else:
                temp.append(A.arr[i])
                i += 1
                j += 1
            
        if i < j:
            while i < len(A.arr):
                temp.append(A.arr[i])
                i += 1
        elif j < i:
            while j < len(B):
                temp.append(B.arr[j])
                j += 1
                
        self.arr = temp
        return temp
        
    def union(self,A,B):
        
        temp = A.arr
        
        for i in B.arr:
            if i not in temp:
                temp.append(i)
        
        self.arr = temp
        
        return temp

    def display(self):
        for i in self.arr:
            print(i, end = " ")
        print()
        
if __name__ == "__main__":
    a = Set()
    b = Set()
    
    li1 = list(map(int,input().split()))
    li2 = list(map(int,input().split()))

    print(li1)
    print(li2)
    
    for i in li1:
        a.insertElement(i)
        
    for i in li2:
        b.insertElement(i)
    a.display()
    b.display()
    
    c = Set()
    d = Set()
    
    c.intersect(a,b)
    d.union(a,b)
    
    c.display()
    d.display()