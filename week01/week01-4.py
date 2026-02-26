# week01-4.py 學習計畫 Array/String第3題
# Leet Code 1431. Kids With the Greatest Number of Candies
# 給額外的extraCandies後,小朋友手上的糖果,會不會是最多的?
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      ans = [] #答案的True 和 False將塞裡面
      best = max(candies) #目前小朋友最多有幾顆糖?
      for candie in candies: #逐一檢查 如果把extraCandies給小朋友
          if candie + extraCandies >= best: ans.append(True)
          else: ans.append(False)#它會不會 >= 最多的,依序塞入 ans
      return ans
