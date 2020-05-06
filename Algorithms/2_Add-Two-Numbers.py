## LeetCode
## https://leetcode.com/problems/two-sum/

# ▼▼ Two Sum ▼▼
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        indexList = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                tempTarget = nums[i] + nums[j]
                if tempTarget == target:
                    indexList.append(i)
                    indexList.append(j)
                    print(indexList)
                    return indexList
                
        print("target is not found in nums.")
        return indexList
                    
# エントリポイント
nums = [2, 3, 1, 7]
target = 9

Solution().twoSum(nums, target)
# ▲▲ Two Sum ▲▲
# ▼▼ Two Sum 解答 ▼▼
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

nums = [2, 3, 1, 7]
target = 9
print(Solution().twoSum(nums, target))
# ▲▲ Two Sum 解答 ▲▲
