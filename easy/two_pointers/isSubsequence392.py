class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        if len(s) == 0:
            return True
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                if i >= len(s):
                    return True
            j += 1
        return False


if __name__ == '__main__':
    test = Solution()
    # s = "abc"
    # t = "ahbgdc"
    s = "axc"
    t = "ahbgdc"
    word = test.isSubsequence(s, t)
    print(word)