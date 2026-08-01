class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [0] * (n + 1)
        counter = Counter(nums)
        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        
        ans = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                ans.extend(bucket[i])
            if len(ans) == k:
                break
        return ans
