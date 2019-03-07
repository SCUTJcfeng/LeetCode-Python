class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        chrList = []
        for string in s:
            if string in chrList:
                maxLen = max(maxLen, len(chrList))
                index = chrList.index(string)
                chrList = chrList[index + 1:]
            chrList.append(string)
        return max(maxLen, len(chrList))


S = Solution()
print(S.lengthOfLongestSubstring("dvdf"))
