# Laboratorium 8: Złożoność obliczeniowa
# Część 4: Zadania MEGA rozszerzone

class SimpleHeap:
    def __init__(self):
        self.heap = [None]
        
    def insert(self, value):
        """Wstaw element do kopca (Max-Heap)"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, index):
        while index > 1:
            parent_idx = index // 2
            if self.heap[index] > self.heap[parent_idx]:
                self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
                index = parent_idx
            else:
                break
                
    def take_max(self):
        """Usuń i zwróć największy element (korzeń)"""
        if len(self.heap) <= 1:
            return None
        max_val = self.heap[1]
        last_val = self.heap.pop()
        
        if len(self.heap) > 1:
            self.heap[1] = last_val
            self._sift_down(1)
            
        return max_val
    
    def _sift_down(self, index):
        while True:
            largest = index
            left = 2 * index
            right = 2 * index + 1
            
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
                
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
                
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

# Testy z zadania
if __name__ == "__main__":
    print("Zadanie 12: Implementacja SimpleHeap (Max-Heap)")
    h = SimpleHeap()
    h.insert(10)
    h.insert(30)
    h.insert(20)
    
    val1 = h.take_max()
    print(f"take_max() -> {val1} (Powinno być 30)")
    
    val2 = h.take_max()
    print(f"take_max() -> {val2} (Powinno być 20)")
    
    val3 = h.take_max()
    print(f"take_max() -> {val3} (Powinno być 10)")