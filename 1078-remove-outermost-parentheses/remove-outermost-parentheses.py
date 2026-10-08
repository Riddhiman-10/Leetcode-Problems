class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        list1=[]
        curr=0
        for i in s:
            if i=='(':
                if curr>0:
                    list1.append(i)
                curr+=1
            elif i==')':
                curr-=1
                if curr>0:
                    list1.append(i)
        return "".join(list1)