"""
@author : Seunghyun
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/
"""
class Solution:
    def __init__(self):
        self.seq = []
        self.invalid = False
    
    def recur(self, sub_words: List[str]):
        if self.invalid: return
        
        if '' in sub_words:
            if sub_words[0] != '':
                self.invalid = True
                return
            else:
                sub_words.pop(0)
        
        sub_list = []
        prev_word = sub_words[0][0]
        lex_seq = [prev_word]
        
        for words in sub_words:
            root_word = words[0]
            
            if root_word == prev_word:
                if len(words) >= 2:
                    sub_list.append(words[1:])
                elif len(sub_list) > 0:
                    sub_list.append('')
            
            else: # 맨 앞의 word 가 바뀔 때마다 recur call
                if len(sub_list) >= 2: # 두개 이상일 때 recur
                    self.recur(sub_list)
                    
                if root_word not in lex_seq: 
                    lex_seq.append(root_word)

                    # initialize
                    if len(words) >= 2:
                        sub_list = [words[1:]]
                    else:
                        sub_list = []
                    prev_word = root_word
                else:
                    self.invalid = True
        
        # # Recursive
        if len(sub_list) > 1:
            self.recur(sub_list)
            
        self.seq.append(''.join(lex_seq))
    
    def alienOrder(self, words: List[str]) -> str:
        self.recur(words)
                
        if self.invalid: # order is invalid
            return ""
        
        self.seq = list(set(self.seq))
        seq_words = ""
        for w in self.seq:
            seq_words += w
        seq_words = set(seq_words)
        
        all_words = ""
        for w in words:
            all_words += w
        all_words = set(all_words)
        remain_words = all_words-seq_words
        
        
        refine = []
        for i in range(len(self.seq)):
            e1 = ''.join(self.seq[i])
            flag = True
            for j in range(len(self.seq)):
                e2 = ''.join(self.seq[j])    
                if i != j:
                    if sorted(e1) == sorted(e2):
                        return ""
                    elif len(e1) <= len(e2):
                        match_cnt = 0
                        for k in range(len(e1)): 
                            if e1[k] in e2: match_cnt += 1
                        if match_cnt == len(e1):
                            flag = False
                            break
                    
            if flag:
                refine.append(self.seq[i])
        
        output = []

        while True:
            flag = False          
            for i in range(len(refine)):
                root = refine[i]
                for j in range(i+1, len(refine)):
                    if root[0] == refine[j][-1]:
                        refine.insert(j+1, root)
                        refine.pop(i)
                        flag = True
                        break
                
            if flag == False: # 종료
                break

        for w in refine:
            new_output = []
            w_exist = []
            w_list = list(w)
            if not output:
                output += w_list
            else:
                for e in w_list:
                    if e in output:
                        w_exist.append(True)
                    else:
                        w_exist.append(False)

                while w_list:
                    w = w_list.pop(0)
                    w_e = w_exist.pop(0)
                    
                    while output:
                        if w_e:
                            o = output.pop(0)
                            new_output.append(o)
                            if w == o: break
                        else:
                            new_output.append(w)
                            break

                    if not w_e and not output:
                        new_output.append(w)

                while output:
                    o = output.pop(0)
                    new_output.append(o)
                    
                output = new_output.copy()
        
        # 포함 안된 것 append
        output = ''.join(output)
        for w in remain_words:
            output += w
        
        return output
