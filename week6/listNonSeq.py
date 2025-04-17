import sys

class ListArrayNonSeq:
    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.arr = [None] * capacity  # 데이터를 저장할 배열
        self.link = [0] * capacity    # 다음 노드의 인덱스를 저장할 배열
        self.first = -1               # 리스트의 첫 번째 요소 인덱스
        self.avail = 0                # 사용 가능한 첫 번째 빈 노드 인덱스
        self.size = 0                 # 리스트의 현재 크기

        # 사용 가능한 노드 리스트 초기화 (링크 연결)
        for i in range(capacity - 1):
            self.link[i] = i + 1
        self.link[capacity - 1] = -1 # 사용 가능한 노드 리스트의 끝 표시

    def _get_node(self):
        """사용 가능한 노드 리스트에서 노드를 할당받습니다."""
        if self.avail == -1:
            return -1 # 사용 가능한 노드가 없음을 나타냄
        node_index = self.avail
        self.avail = self.link[self.avail] # avail을 다음 빈 노드로 업데이트
        return node_index

    def _free_node(self, index):
        """사용했던 노드를 사용 가능한 노드 리스트의 맨 앞에 반환합니다."""
        if index < 0 or index >= self.capacity:
             # 정상적인 경우 발생하지 않지만, 견고성을 위해 추가
             print(f"Warning: Attempting to free invalid index {index}", file=sys.stderr)
             return

        # 반환된 노드를 avail 리스트의 시작 부분에 추가
        self.link[index] = self.avail
        self.avail = index

    def __len__(self):
        """리스트에 있는 요소의 수를 반환합니다."""
        return self.size

    def _insert_logic(self, data, new_node):
        """정렬 순서를 유지하며 미리 할당된 노드에 데이터를 삽입하는 내부 로직입니다."""
        self.arr[new_node] = data
        prev = -1
        curr = self.first

        # 정렬된 순서에 맞는 삽입 위치 탐색
        while curr != -1 and self.arr[curr] < data:
            prev = curr
            curr = self.link[curr]

        # 새 노드 삽입
        if prev == -1: # 리스트의 맨 앞에 삽입
            self.link[new_node] = self.first
            self.first = new_node
        else: # 리스트의 중간 또는 맨 끝에 삽입
            self.link[new_node] = self.link[prev] # curr과 동일
            self.link[prev] = new_node

        self.size += 1


    def add(self, data):
        """리스트에 데이터를 정렬된 순서로 추가합니다. 리스트가 가득 차면 예외를 발생시킵니다."""
        new_node = self._get_node()
        if new_node == -1:
            raise Exception("add from full array")
        self._insert_logic(data, new_node)


    def insert(self, data):
        """리스트에 데이터를 정렬된 순서로 삽입합니다. 리스트가 가득 차면 예외를 발생시킵니다."""
        new_node = self._get_node()
        if new_node == -1:
            raise Exception("insert from full array")
        self._insert_logic(data, new_node)

    def delete(self, data):
        """리스트에서 데이터의 첫 번째 발생을 삭제합니다."""
        prev = -1
        curr = self.first

        # 삭제할 노드 탐색
        while curr != -1 and self.arr[curr] != data:
            prev = curr
            curr = self.link[curr]

        # 데이터를 찾은 경우
        if curr != -1:
            # 노드 연결 해제
            if prev == -1: # 첫 번째 노드 삭제
                self.first = self.link[curr]
            else: # 중간 또는 마지막 노드 삭제
                self.link[prev] = self.link[curr]

            # 노드 반환
            self._free_node(curr)
            self.size -= 1
        # 데이터를 찾지 못한 경우 아무 작업도 하지 않음

    def __repr__(self):
        """리스트의 문자열 표현을 반환합니다."""
        elements = []
        curr = self.first
        while curr != -1:
            elements.append(str(self.arr[curr])) # 다양한 타입의 데이터를 위해 str() 사용
            curr = self.link[curr]
        return f"[{', '.join(elements)}]"

# 제공된 테스트 코드 유지
if __name__ == "__main__":
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
        # 리스트가 가득 참 (크기 6)
        lst.add("I") # "add from full array" 예외 발생해야 함
        print(f"lst[{len(lst)}] = {lst}")
    except Exception as e:
        print(e) # "add from full array" 출력 예상

    try:
        lst.insert("G") # "insert from full array" 예외 발생해야 함
        print(f"lst[{len(lst)}] = {lst}")
    except Exception as e:
        print(e) # "insert from full array" 출력 예상

    # 삭제 및 삽입 계속
    lst.delete("A")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("E")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("G") # 이제 성공해야 함
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("C")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("F")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("G")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("B")
    print(f"lst[{len(lst)}] = {lst}")
    lst.delete("H") # 리스트가 비어 있어야 함
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("E")
    print(f"lst[{len(lst)}] = {lst}")
    lst.insert("F")
    print(f"lst[{len(lst)}] = {lst}")
