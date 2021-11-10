class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        char_cnt = collections.Counter(s)
        char_cnt = sorted([(cnt, ch) for ch, cnt in char_cnt.items() ])
        max_freq = char_cnt[-1][0]
        ans_lst = ["" for _ in range(max_freq) ]
        
        idx = 0
        while char_cnt:
            cnt, ch = char_cnt.pop()
            if cnt == max_freq:
                for i in range(max_freq):
                    ans_lst[i] += ch
            else:
                while cnt:
                    slot = idx%(max_freq-1)
                    ans_lst[slot] += ch
                    idx+=1
                    cnt -= 1
        
        for i in range(len(ans_lst)-1):
            if len(ans_lst[i]) < k:
                return ''
        return "".join(ans_lst)
                
