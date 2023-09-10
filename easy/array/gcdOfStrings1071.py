import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)
        i = j = 0
        factor1 = ''
        gcd1 = []
        factor2 = ''
        gcd2 = []
        while i < str1_length:
            factor1+=str1[i]
            if str1_length % len(str1)==0:
                multiple = str1_length//len(factor1)
                if factor1*multiple == str1:
                    gcd1.append(factor1)
            i+=1
        while j < str2_length:
            factor2+=str2[j]
            if str2_length % len(str2)==0:
                multiple = str2_length//len(factor2)
                if factor2*multiple == str2:
                    gcd2.append(factor2)
            j+=1
        
        ans = ''
        reversed_gcd1 = gcd1[::-1]
        for factor1 in reversed_gcd1:
            if factor1 in gcd2:
                ans = factor1
                return ans
        return ""

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if candidate * (len(str1) // candidate_len) == str1 and candidate * (len(str2) // candidate_len) == str2:
            return candidate
        return ''



if __name__ == '__main__':
    test = Solution()
    # word1 = 'ABCABCABC'
    # word2 = 'ABC'
    word1 = 'ABAB'
    word2 = 'AB'
    # word1 = 'LEET'
    # word2 = 'CODE'
    # word1 = 'AAAAAA'
    # word2 = 'AAA'
    word = test.gcdOfStrings2(word1, word2)
    print(word)