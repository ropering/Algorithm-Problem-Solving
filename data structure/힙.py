
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 인덱스 번호는 1번부터
        self.heap_array.append(data)

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        if left_child_popped_idx >= len(self.heap_array): # 리스트의 길이가 2 ..... 이하라면
            return False # 값이 1개 이하이므로 이동 X
        elif right_child_popped_idx >= len(self.heap_array): # 리스트의 길이가 3 .... 이하라면
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # 부모노드 값이 왼쪽 자식 노드 값보다 작다면
                return True
            else:
                return False
        else: # 리스트의 길이가 4 이상이라면
            # 자식노드의 왼쪽, 오른쪽은 크기 구분을 하지 않으므로 if-else로 각각 만들어주어야 한다
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # 부모 노드 값 < 왼쪽 자식 노드 값
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False
        
    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1
        
        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            if right_child_popped_idx >= len(self.heap_array): #???
                self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                # 상위 popped_idx 와 while의 popped_idx는 다르다
                poppoed_idx = left_child_popped_idx # while의 popped_idx를 가리키는 것
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # 왼쪽 노드 <-> 부모 노드
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    # 비교할 위치로 이동 (아래)
                    poppoed_idx = left_child_popped_idx
                else:
                    # 오른쪽 노드 <-> 부모 노드
                    self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                    # 비교할 위치로 이동 (아래)
                    poppoed_idx = right_child_popped_idx
        
        return returned_data
    
    # 삭제 보다 단순한 이유  
    # 삽입 : 부모 끼리만 비교하면 되기 때문
    # 삭제 : 왼쪽, 오른쪽 자식 둘 다 비교해야 하기 때문
    def move_up(self, inserted_idx):
        if inserted_idx <= 1: # 현재 인덱스가 최상위 노드라면
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]: # 현재값 > 부모값
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1 # 인덱스 0을 빼준 것 (None) 마지막 인덱스 == 현재 인덱스
        
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx # 다음 비교할 인덱스로 이동 (부모 인덱스)
        return True
    
heap = Heap(3)
heap.heap_arrayteams

heap.insert(5)
heap.heap_array

heap.pop()
heap.heap_array


import heapq
heap = []
heapq.heappush(heap, 3)
type(heap)


