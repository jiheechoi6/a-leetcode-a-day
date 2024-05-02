class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                s1 = s[0:left] + s[left+1:]
                s2 = s[0:right] + s[right+1:]

                return s1 == s1[::-1] or s2 == s2[::-1]
            else:
                left +=1
                right -=1
        
        return True
      
