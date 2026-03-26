# week01-5.py 學習計畫 Array/String第7題
# LeetCode 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        preSum = [1]
        postSum =[1]
        for i in range(N):
            preSum.append( preSum[-1] * nums[i])
            postSum.append( postSum[-1] * nums[N-1-i])
            #print(postSum) #print(preSum)
        ans = []
        for i in range(N):
            ans.append( preSum[i] *postSum[N-1-i])
        return ans
class Solution:
