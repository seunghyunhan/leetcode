"""
@author : Seunghyun
604. Design Compressed String Iterator
https://leetcode.com/problems/design-compressed-string-iterator/
"""
class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.ch = ''
        self.ptr = 0
        self.counter = 0
        self.str_len = len(self.compressedString)

    def next(self) -> str:
        if self.hasNext():
            if self.counter == 0:
                digit = []
                ch_flag = False
                digit_flag = False
                
                self.ch = self.compressedString[self.ptr]
                while True:
                    self.ptr += 1
                    if self.ptr >= self.str_len:
                        break
                        
                    ch = self.compressedString[self.ptr]
                    if ch >= '0' and ch <= '9':        
                        digit.append(ch)
                    else:
                        break                            
                
                self.counter = int(''.join(digit))
                # print (self.ch, self.counter)
            self.counter -= 1
            return self.ch
        else:
            return ' '

    def hasNext(self) -> bool:
        if self.counter > 0 or self.str_len > self.ptr:
            return True
        else:
            return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
