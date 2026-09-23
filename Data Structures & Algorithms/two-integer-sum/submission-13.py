class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for key, value in enumerate(nums):
            result = target - value
            if result in seen:
                return [seen[result], key]
            seen[value] = key