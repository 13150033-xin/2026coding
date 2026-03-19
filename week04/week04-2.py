# week04-2.py 學習計畫 Prefix Sum第1題
# LeetCode 1732. Find the Highest Altitude
#找到最高的海拔高度(一直加,就好了!)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N=len(gain) #陣列的長度N
        ans=H=0 #一開始高度是0
        #答案一開始是0,因為一開始高度是0
        for i in range(N): #逐個加起來
            H += gain[i] #現在增減的量 gain[i] 加進H
            ans=max(ans, H) #更新最高的答案
        return ans
