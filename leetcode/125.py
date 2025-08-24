class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s="".join(char.lower() for char in s if char.isalnum())
        if not clean_s:
            return True
        left=0
        right=len(clean_s)-1
        while left<right:
            if clean_s[left]!=clean_s[right]:
                return False
            left+=1
            right-=1
        return True