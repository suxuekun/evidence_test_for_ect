class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [nums[0],max(nums[0] + nums[1],nums[0]-nums[1])]

        for i in range(2,n):
            dp.append(max(dp[i-2] + nums[i-1]-nums[i], dp[i-1] + nums[i]))
        return dp[n-1]