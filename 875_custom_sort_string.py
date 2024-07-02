class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        slist = [o*cnt.pop(o, 0) for o in order]

        for remain, rcount in cnt.items():
            slist.append(remain * rcount)

        return ''.join(slist)
