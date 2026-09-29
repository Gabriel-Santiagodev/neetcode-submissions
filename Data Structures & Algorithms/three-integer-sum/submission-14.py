class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        res = 0
        L = 0
        R = len(nums_sorted) - 1
        lst = []     
        seen = set()
        
        for i in range(len(nums_sorted)):
            if nums_sorted[i] in seen:
                continue
            seen.add(nums_sorted[i])
            L = i + 1
            
            while L < R:
                res = nums_sorted[i] + nums_sorted[L] + nums_sorted[R]

                if res == 0:
                    lst.append(sorted([nums_sorted[i], nums_sorted[L], nums_sorted[R]]))
                    R-=1
                    L+=1
                    while  L < R:
                        if nums_sorted[L] == nums_sorted[L-1]:
                            L+=1
                        else:
                            break
                        
                if res > 0:
                    R-=1
                if res < 0:
                    L +=1
            R = len(nums_sorted) - 1
        
        return lst
        