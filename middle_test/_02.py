


class CircleQueue:

    def __init__(self, capacity = 5):
        self.list = [] * capacity
        

    def push(self):
        
        data = None

        if len(self.list) >= 2:
            size = len(self.list)
            data = self.list[size-1] + self.list[size-2]
            self.list.append(data)
        elif len(self.list) == 1:
            self.list.append(1)
            data = 1
        else:
            self.list.append(0)
            data = 0

        print(f"Fibo({len(self.list) - 1}) = {data}")
    
    
    
    


if __name__ == "__main__":
    cq = CircleQueue()

    for _ in range(12):
        cq.push()