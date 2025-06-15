class Stack:

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.arr = [0 for _ in range(capacity)]
        self.top = -1

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def full(self):
        if self.top >= self.capacity - 1:
            return True
        else:
            return False
    
    def push(self,item):
        if self.full():
            return
        else:
            self.top += 1
            self.arr[self.top] = item
    
    def peek(self):
        if self.empty():
            return None
        else:
            return self.arr[self.top]
    
    def pop(self):
        if self.empty():
            return 
        temp = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return temp
    
    def __len__(self):
        if self.empty():
            return 0
        else:
            return self.top + 1
    
    def __repr__(self):
        return str(self.arr)
        

class PostFixEval:
    OPS = ("+", "-", "*", "/")
           
    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        stack = Stack(len(self.expr))
        for tok in self.expr:
            if tok not in self.OPS:
                stack.push( int(tok))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.push(self.cal(tok,n1,n2))
        
        return stack.pop()

        
    def cal(self, op, v01, v02) -> int:

        if op == '+':
            return v01 + v02
        elif op == '-':
            return v01 - v02
        elif op == '*':
            return v01 * v02
        else:
            return v01 // v02
        

import logging

if __name__ == "__main__":
    expr = "6523+8*+3+*"
    postfix = PostFixEval(expr)
    res = postfix.eval()
    logging.info(f"PostFix({expr}).eval = {res}")
    print(res)
    expr = "34*25*+"
    postfix = PostFixEval(expr)
    res = postfix.eval()
    print(res)
    logging.info(f"PostFix({expr}).eval = {res}")
    