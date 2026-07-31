class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + val
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[r], val])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans