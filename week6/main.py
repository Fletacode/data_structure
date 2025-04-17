class ListArrayNonSeq:

    def __init__(self, capacity=5):
        self.arr = [0 for i in range(capacity)]
        self.link = [0 for i in range(capacity)]
        self.first = -1
        self.length = 0
        self.start = 0
        self.capacity = capacity

    def randon_idx(self):
        for i in range(self.capacity):
            if self.arr[i] == 0:
                return i

    def delete(self, data):

        find_idx = 0

        for (idx, item) in enumerate(self.arr):
            if item == data:
                find_idx = idx
                self.arr[find_idx] = 0
                break

        back_idx = 0

        for (idx,item) in enumerate(self.link):
            if (find_idx == item):
                back_idx = idx
                break


        front_idx = self.link[find_idx]
        self.link[find_idx] = -1
        self.link[back_idx] = front_idx
        self.length -= 1
        # print(front_idx)
        # print(back_idx)




    def add(self, data):
        if self.full():
            raise IndexError("add from full array")

        idx = self.randon_idx()
        self.arr[idx] = data
        self.link[idx] = -1
        if not self.empty():
            self.link[self.first] = idx
        else:
            self.start = idx

        self.first = idx
        self.length += 1

    def insert(self, data):
        if self.full():
            raise IndexError("insert from full array")
        else:
            self.add(data)


    def full(self):
        return self.length == self.capacity


    def __len__(self):
        return self.length

    def empty(self):
        return self.length == 0

    def __repr__(self):
        if self.empty():
            return str([])

        temp = []
        temp.append(self.arr[self.start])
        idx = self.link[self.start]

        while idx != -1:
            temp.append(self.arr[idx])
            idx = self.link[idx]

        return str(temp)

if __name__ == '__main__':
    SIZE = 6
    lst = ListArrayNonSeq(SIZE)
    try:
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("B")
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("E")
        print(f"lst[{len(lst)}] = {lst}")
        lst.insert("F")
        print(f"lst[{len(lst)}] = {lst}")
        lst.insert("C")
        print(f"lst[{len(lst)}] = {lst}")
        lst.insert("A")
        print(f"lst[{len(lst)}] = {lst}")
        lst.add("H")
        print(f"lst[{len(lst)}] = {lst}")

        lst.add("I")
        print(f"lst[{len(lst)}] = {lst}")

    except Exception as e:
        print(e)
    try:
        lst.insert("G")

    except Exception as e:
        print(e)

    lst.delete("A")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("E")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("G")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("C")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("F")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("G")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("B")
    print(str(lst.arr))
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("H")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("E")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("F")
    print(f"lst[{len(lst)}] = {lst}")
