class Solution:
    def maxDepth(self, s: str) -> int:
        max_c=0
        c=0
        for i in s:
            if i=='(':
                c+=1
            elif i==")":
                c-=1
            else:
                continue
            max_c= max(max_c,c)
        return max_c