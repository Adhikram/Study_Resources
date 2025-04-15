class MaxHeap:
    """
    A Max Heap implementation with standard operations.
    
    Time Complexity:
    - Insertion: O(log n)
    - Extract Max: O(log n)
    - Get Max: O(1)
    - Heapify: O(n)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self):
        """Initialize an empty max heap."""
        self.heap = []
    
    def parent(self, i: int) -> int:
        """Return the index of the parent of node at index i."""
        return (i - 1) // 2
    
    def left_child(self, i: int) -> int:
        """Return the index of the left child of node at index i."""
        return 2 * i + 1
    
    def right_child(self, i: int) -> int:
        """Return the index of the right child of node at index i."""
        return 2 * i + 2
    
    def swap(self, i: int, j: int) -> None:
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key) -> None:
        """Insert a new key into the max heap."""
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i: int) -> None:
        """Move a node up in the tree to maintain heap property."""
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def extract_max(self):
        """
        Remove and return the maximum element from the heap.
        Raises ValueError if heap is empty.
        """
        if len(self.heap) == 0:
            raise ValueError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return max_val
    
    def _sift_down(self, i: int) -> None:
        """Move a node down in the tree to maintain heap property."""
        max_index = i
        size = len(self.heap)
        
        left = self.left_child(i)
        if left < size and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        right = self.right_child(i)
        if right < size and self.heap[right] > self.heap[max_index]:
            max_index = right
        
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)
    
    def get_max(self):
        """
        Return the maximum element without removing it.
        Raises ValueError if heap is empty.
        """
        if len(self.heap) == 0:
            raise ValueError("Heap is empty")
        return self.heap[0]
    
    def remove(self, i: int):
        """
        Remove element at index i.
        Raises IndexError if index is out of bounds.
        """
        if i < 0 or i >= len(self.heap):
            raise IndexError("Index out of bounds")
        
        self.heap[i] = float('inf')
        self._sift_up(i)
        self.extract_max()
    
    @classmethod
    def heapify(cls, array: list) -> 'MaxHeap':
        """Create a max heap from an array in O(n) time."""
        heap = cls()
        heap.heap = array.copy()
        
        # Start from last non-leaf node and sift down
        for i in range(len(array) // 2 - 1, -1, -1):
            heap._sift_down(i)
        
        return heap
    
    def is_empty(self) -> bool:
        """Return True if the heap is empty, False otherwise."""
        return len(self.heap) == 0
    
    def get_size(self) -> int:
        """Return the number of elements in the heap."""
        return len(self.heap)
    
    def clear(self) -> None:
        """Remove all elements from the heap."""
        self.heap = []
    
    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self.heap)
    
    def __str__(self) -> str:
        """Return a string representation of the heap."""
        return str(self.heap)

# Example usage
if __name__ == "__main__":
    # Create a new max heap
    heap = MaxHeap()
    
    # Insert some values
    values = [4, 10, 3, 5, 1]
    for value in values:
        heap.insert(value)
    
    print("Heap after insertions:", heap)  # Output: [10, 5, 3, 4, 1]
    
    # Get maximum
    print("Maximum value:", heap.get_max())  # Output: 10
    
    # Extract maximum
    max_val = heap.extract_max()
    print("Extracted max value:", max_val)  # Output: 10
    print("Heap after extract_max:", heap)  # Output: [5, 4, 3, 1]
    
    # Create heap from array
    array = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    heap = MaxHeap.heapify(array)
    print("Heapified array:", heap)  # Output: [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
    
    # Remove from specific index
    heap.remove(1)  # Remove 15
    print("After removing element at index 1:", heap)
    
    # Check if empty and size
    print("Is heap empty?", heap.is_empty())  # Output: False
    print("Heap size:", len(heap))  # Output: 10 