class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        table = {
            'R': 1,
            'L': -1,
            'U': 1.5,
            'D': -1.5
        }
        sum = 0
        for move in moves:
            sum += table[move]
        return sum==0

so = Solution()
print(so.judgeCircle('RRLUD'))
