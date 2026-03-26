# week05-6.py 學習計畫 Hash Table (Map/Set)
# LeetCode 2352. Equal Row and Column Pairs
# 橫的、直的,完全相同「有幾組」
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter() #Hash Map可以知道有哪些row出現幾次
        for row in grid:
            #tuple()把陣列[3,1,2,2],變不會動(3,1,2,2)
            counter[ tuple(row) ] += 1

        ans = 0 #有幾組
        for col in zip(*grid):
            ans += counter[ tuple(col) ]
        return ans
