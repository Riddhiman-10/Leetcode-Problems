class Solution:
    def reverseVowels(self, s: str) -> str:
        char=list(s)
        lt=0
        rt=len(s)-1
        vowels=set('aeiouAEIOU')
        while lt<rt:
            if char[lt] not in vowels:
                lt+=1
            elif char[rt] not in vowels:
                rt-=1
            else:
                char[lt],char[rt]=char[rt],char[lt]
                lt+=1
                rt-=1
        return "".join(char)