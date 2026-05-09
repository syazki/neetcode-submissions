class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    indices.extend([i,j])
                    break
            if len(indices) > 0:
                break
        return indices