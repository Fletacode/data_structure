


class TempQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, data):
        self.stack_in.append(data)

    def dequeue(self):

        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                temp = self.stack_in.pop()
                self.stack_out.append(temp)
            return self.staccu

    q = TempQueue()

    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
