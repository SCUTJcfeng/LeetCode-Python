class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # print(x^y)
        return bin(x^y).count('1')

so = Solution()
print(so.hammingDistance(4, 14))