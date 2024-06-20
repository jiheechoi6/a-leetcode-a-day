class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        max_letter = max(cnt, key = cnt.get)
        res = ['' for _ in range(len(s))]

        if cnt[max_letter] > ((len(s)+1)//2):
            return ""

        idx = 0
        while cnt[max_letter]:
            res[idx] = max_letter
            idx += 2
            cnt[max_letter] -= 1

        for letter, _ in cnt.items():
            while cnt.get(letter):
                if idx >= len(s): idx = 1

                res[idx] = letter
                cnt[letter] -= 1

                idx += 2

        return ''.join(res)
        
