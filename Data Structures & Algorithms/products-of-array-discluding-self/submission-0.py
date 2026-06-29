class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preffix = [1]
        suffix = [1]
        output = []
        for i in range(len(nums)):
            i += 1
            if i == len(nums):
                break
            preffix.append(preffix[i-1] * nums[i-1])
        nums = nums[::-1]
        for j in range(len(nums)):
            j += 1
            if j == len(nums):
                break
            suffix.append(suffix[j-1] * nums[j-1])
        suffix = suffix[::-1]
        nums = nums[::-1]
        for k in range(len(nums)):
            output.append(preffix[k] * suffix[k])
        return output
