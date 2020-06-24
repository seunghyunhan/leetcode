# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:
import queue

class Solution:
    def __init__(self):
        self.queue = queue.Queue()
    
    def read(self, buf: List[str], n: int) -> int:
        if n < 0: return 0
        
        while self.queue.qsize() < n:
            size_read4 = read4(buf)
            if size_read4 == 0: break
            for i in range(size_read4):
                self.queue.put(buf[i])
        
        size_read = min(n, self.queue.qsize())
        for i in range(size_read):
            buf[i] = self.queue.get()
        
        return size_read
