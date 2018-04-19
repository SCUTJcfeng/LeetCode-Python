class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        n = 0
        if x > 0:
            flag = 1
        else:
            flag = -1
        x = x * flag
        lt = []
        while x:
            lt.append(x % 10)
            x = int(x / 10)
            n += 1
        for i in lt:
            sum += i * pow(10, n-1)
            n -= 1

        if sum > pow(2, 31) - 1 or sum < -pow(2, 31):
            return 0

        if flag == -1:
            return -sum
        else:
            return sum

so = Solution()
print(so.reverse(-4874115641))