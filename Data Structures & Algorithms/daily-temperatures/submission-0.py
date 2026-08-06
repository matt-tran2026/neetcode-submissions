class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i, t in enumerate (temperatures):
            while stack and t > stack[-1][0]:
                stack_T, stack_I = stack.pop()
                ans[stack_I] = i - stack_I
            stack.append((t, i))
        return ans