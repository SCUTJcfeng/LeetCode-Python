# class Solution:
#     def __init__(self):
#         self.table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
#                  "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
#         self.alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     def uniqueMorseRepresentations(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
#         morse_code_set = set()
#         for word in words:
#             morse_code = ''
#             for alpha in word:
#                 idx = self.alpha.index(alpha)
#                 morse_code += self.table[idx]
#             morse_code_set.add(morse_code)
#         return len(morse_code_set)

class Solution:
    def __init__(self):
        self.table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code_set = set()
        for word in words:
            morse_code = ''
            for alpha in word:
                morse_code += self.table[ord(alpha) - ord('a')]
            morse_code_set.add(morse_code)
        return len(morse_code_set)

so = Solution()
print(so.uniqueMorseRepresentations([]))
