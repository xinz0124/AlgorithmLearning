from typing import List
class Solution:
    def findDifference_Zhao(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        for num1 in nums1:
            if num1 not in nums2 and num1 not in answer[0]:
                answer[0].append(num1)
        
        for num2 in nums2:
            if num2 not in nums1 and num2 not in answer[1]:
                answer[1].append(num2)
        return answer

    def findDifference_HashSet(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        为了较快地判断一个数组的某个元素是否在另一个数组中存在，我们可以用哈希集合来存储数组的元素。
        在Python中，set是一种无序、不重复元素的集合数据类型。它类似于数学中的集合，可以进行交集、并集、差集等集合操作。
        这里case2下，set将重复的元素去掉了 （并集）
        '''
        set1 = set(nums1)   # nums1 所有元素的哈希集合
        set2 = set(nums2)   # nums2 所有元素的哈希集合
        res = [[], []]
        print(set1)
        print(set2)
        for num in set1:
            if num not in set2:
                res[0].append(num)
        for num in set2:
            if num not in set1:
                res[1].append(num)
        return res
if __name__ == '__main__':
    test = Solution()
    # nums1 = [1,2,3]
    # nums2 = [2,4,6]
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]

    answer = test.findDifference_HashSet(nums1, nums2)
    print(answer)
    print(answer[0])
    print(answer[1])