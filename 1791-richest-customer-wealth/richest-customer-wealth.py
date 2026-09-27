class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m_sum=0
        for i in accounts:
            m_sum=max(m_sum,sum(i))
        return m_sum