
class Solution:
    def splitArray(self, nums, k):
        def canSplit(max_sum):
            subarrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > max_sum:
                    subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num

            return subarrays <= k

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid  
            else:
                left = mid + 1

        return left
