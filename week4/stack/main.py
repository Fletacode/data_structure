from typing import List, Optional

import logging

class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr: List[Optional[int]] = [None] * capacity
        self.top = -1

    def __len__(self):
        return self.top + 1

    def empty(self) -> bool:
        if (self.top == -1):
            return True
        else:
            return False

    def full(self) -> bool:
        if (self.top == self.capacity - 1):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return str(self.arr[:self.top + 1])

    def push(self, num : int) -> None:
        if (self.full()):
            raise IndexError("push from full stack")
        self.top += 1
        self.arr[self.top] = num


    def peek(self) -> Optional[int]:
        if (self.empty()):
            raise IndexError("peek from empty stack")

        return self.arr[self.top]

    def pop(self) -> Optional[int]:
        if (self.empty()):
            raise IndexError("peek from empty stack")

        temp = self.arr[self.top]
        self.top -= 1
        return temp

    def infix_to_postfix(self,expr: str) -> str:
        OPS = ("+", "-", "*", "/", "^", "(", ")")
        PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": -9, ")":-9}
        stack = Stack(len(expr))

        ret = []

        for token in expr:
            if (token in OPS):

                if token == "(":
                    stack.push(token)
                elif token == ")":
                    while not stack.empty() and stack.peek() != "(":
                        ret.append(stack.pop())
                    stack.pop()
                else:
                    while not stack.empty() and PREC[stack.peek()] >= PREC[token]:
                        ret.append(stack.pop())
                    stack.push(token)
            else:
                ret.append(token)

        while not stack.empty():
            ret.append(stack.pop())

        return "".join(ret)


class PostFixEval:
    OPS = ("+", "-", "*", "/")

    def __init__(self, expr):
        self.expr = expr


    def cal(self, op, val1, val2) -> int:
        if (op == self.OPS[0]):
            return int(val1) + int(val2)
        elif (op == self.OPS[1]):
            return int(val1) - int(val2)
        elif (op == self.OPS[2]):
            return int(val1) * int(val2)
        else:
            return int(val1) / int(val2)

    def eval(self) -> Optional[int]:
        stack = Stack(len(self.expr))

        for token in self.expr:
            if (stack.empty()):
                stack.push(token)
                continue

            if (token in self.OPS):
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.push(self.cal(token, temp1, temp2))
            else:
                stack.push(token)

        return stack.pop()



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    SIZE = 5
    stack = Stack(SIZE)
    logging.info(f"stack({len(stack)}): {stack}")
    logging.info(f"stack.empty: {stack.empty()}")
    try:
        elem = stack.peek()
        logging.info(f"stack.peek() = {elem}")
    except Exception as e:
        logging.exception(e)
    try:
        for i in range(1, SIZE + 2):
            stack.push(i)
            logging.info(f"stack.push({i})")
            logging.info(f"stack({len(stack)}): {stack}")
    except Exception as e:
        logging.exception(e)
        logging.info(f"stack.empty: {stack.empty()}")

    try:
        expr = "6523+8*+3+*"
        postfix = PostFixEval(expr)
        res = postfix.eval()
        logging.info(f"PostFix({expr}).eval = {res}")
        expr = "34*25*+"
        postfix = PostFixEval(expr)
        res = postfix.eval()
        logging.info(f"PostFix({expr}).eval = {res}")
    except Exception as e:
        logging.exception(e)

    stack = Stack(10)
    expr = "1*(2+3)*4"
    postfix = stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1*2+3*4"
    postfix = stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1+2*3"
    postfix = stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1*2+3"
    postfix = stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1+(2*3+4)*5"
    postfix = stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")

