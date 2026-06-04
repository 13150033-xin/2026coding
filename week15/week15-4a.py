# week15-4a.py 學習計畫 DP - Multidimensional 第4題
# LeetCode 72. Edit Distance 編輯(插入1字母、刪掉1字母、換掉1字母)幾次後,會得到 word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N =len(word1), len(word2) # 兩字串的長度
        @cache
        def helper(i,j): # 現在要處理 word1[i] vs. word2[j]
            if i==M and j==N: return 0 # 都走到最後
            if i==M: return N-j # word2剩下的,都要刪掉
            if j==N: return M-i # word1剩下的,都要刪掉
            if word1[i]==word2[j]: return helper(i+1,j+1) # 直達車
            #ans1 = helper(i+1, j) # 跳掉word1[i]
            #ans2 = helper(i, j+1) # 跳掉word2[j]
            #ans3 = helper(i+1, j+1) # 將word1[i]換成word2[j]
            return min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1))  + 1
        return helper(0,0)
