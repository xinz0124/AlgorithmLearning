class Solution:
    def mergeAlternately_Zhao(self, word1: str, word2: str) -> str:
        '''
        这是 作者第一次做算法题，白纸状态下 的答案；
        应该是 暴力解法了
        '''
        word1_length = len(word1)
        word2_length = len(word2)
        word_limits = [1, 100] 
        word_merge = ''
        for i in range(word_limits[1]):
            if i < word1_length:
                word_merge+=word1[i]
                
            if i < word2_length:
                word_merge+=word2[i]

        return word_merge

    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        这是 官方的解题思路
        双指针方法
        时间复杂度 O(m+n)
        空间复杂度 O(1) 或 O(m+n)
        注意 "".join()
        '''
        m, n = len(word1), len(word2)
        i = j = 0

        ans = list()
        while i < m or j < n:
            if i < m:
                ans.append(word1[i])
                i += 1
            if j < n:
                ans.append(word2[j])
                j += 1
        
        return "".join(ans)


if __name__ == '__main__':
    test = Solution()
    word1 = 'abc'
    word2 = 'pqr'
    word = test.mergeAlternately(word1, word2)
    print(word)