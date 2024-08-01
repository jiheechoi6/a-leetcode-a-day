class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keymap = {}
        keyval = ord('a')

        for ch in key:
            if ch != ' ' and ch not in keymap:
                keymap[ch] = chr(keyval)
                keyval += 1

        res = ''
        for ch in message:
            if ch == ' ': res += ' '
            else: res += keymap[ch]

        return res
        
