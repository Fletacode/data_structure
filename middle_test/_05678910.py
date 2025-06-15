class DlistNode:

    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None

def init(H:DlistNode, T:DlistNode):
    H.next = T
    T.prev = H


def print_list(H:DlistNode, T:DlistNode):
    p = H.next
    while p != T:
        print(f"[{p.data}] " +  ( " <=> " if p.next != T else "" ) , end="")
        p = p.next
    print()


def insert(H:DlistNode, T:DlistNode, pos = 1, data = None):
    node = DlistNode(data)

    now = H
  
    for _ in range(1,pos+1):
        if now == T:
            break
        now = now.next

    node.next = now
    node.prev = now.prev
    now.prev.next = node
    now.prev = node

    
def insertTail(H,T, pos, data):
    node = DlistNode(data)

    now = T
    for _ in range(1,pos + 1):
        now = now.prev

    node.next = now.next
    node.prev = now
    now.next.prev = node
    now.next = node
    

def printRotate(H,T, count):

    now = H

    for i in range(count):
        if now.data is None:
            now = now.next
        print(f"[{now.data}]" + (" <=> " if i != count-1 else ""), end="")
        now = now.next
    print()

def delete(H,T,k):


    now = H.next
    while now is not T:
        if now.data == k:
            now.prev.next = now.next
            now.next.prev = now.prev
        now = now.next

def switchElement(H, pos1,pos2, direction):
    
    if direction == 'r':
        p = H
        for _ in range(1,pos1+1):
            if p.next.data is None:
                p = p.next
            p = p.next
        
        node1 = p

        for _ in range(pos2):
            if p.next.data is None:
                p = p.next
            p = p.next

        node2 = p

        node1.data, node2.data = node2.data, node1.data
    else:
        p = H
        for _ in range(1,pos1+1):
            if p.next.data is None:
                p = p.next
            p = p.next
        
        node1 = p

        for _ in range(pos2):
            if p.prev.data is None:
                p = p.prev
            p = p.prev

        node2 = p

        node1.data, node2.data = node2.data, node1.data

if __name__ == "__main__":
    h = DlistNode()
    t = DlistNode()
    init(h,t)
    insert(h,t,1,10)
    insert(h,t,1,20)
    insert(h,t,2,30)
    insert(h,t,4,40)
    insert(h,t,3,50)
    print_list(h,t)

    h.prev = t.prev
    t.next = h.next    
    
    print("[%d] [%d]\n", h.prev.data, t.next.data)

    insertTail(h,t,1,10)
    insertTail(h,t,3,60)
    insertTail(h,t,4,50)
    print_list(h,t)

    printRotate(h,t,10)

    delete(h,t,50)
    print_list(h,t)

    switchElement(h,2,3,'r')
    switchElement(h,4,2,'l')
    print_list(h,t)
