class Solution:
    def reverseString(self, s: list[str]) -> None:
        first=0
        last=len(s)-1
        x=len(s)
        for _ in range(int(x//2)):
            temp=s[first]
            s[first]=s[last]
            s[last]=temp
            first+=1
            last-=1