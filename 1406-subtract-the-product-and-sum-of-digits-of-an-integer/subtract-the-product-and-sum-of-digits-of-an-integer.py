class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        suum=0
        prod=1
        for i in str(n):
            prod*=int(i)
            suum+=int(i)
        return prod-suum