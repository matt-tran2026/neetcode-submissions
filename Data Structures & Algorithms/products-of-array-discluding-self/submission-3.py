class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        length = len(nums)
        l_arr = [0] * length
        r_arr = [0] * length 

        for i in range(length):
            j = -i -1 
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        res = []
        for i in range(length):
            res.append(l_arr[i] * r_arr[i])
        return res