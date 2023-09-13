from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences_Zhao(self, arr: List[int]) -> bool:
        key_list = []
        value_list = []
        for val in arr:
            if val not in key_list:
                key_list.append(val)
                size = len([x for x in arr if x == val])
                value_list.append(size)
        if  len(value_list) == len(set(value_list)):
            return True
        else:
            return False

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        print(Counter(arr).values())
        print(Counter(Counter(arr).values()).values())
        return all(i==1 for i in Counter(Counter(arr).values()).values())

if __name__ == '__main__':
    # arr = [1,2,2,1,1,3]
    arr = [1,2]
    # arr = [-3,0,1,-3,1,1,1,-3,10,0]
    test = Solution()
    print(test.uniqueOccurrences(arr))