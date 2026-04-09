# week07-3.py 學習計畫 Stack 第1題
# LeetCode 2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        ans=[] # 用來放答案的陣列 list 其實有stack性質
        for c in s: # 逐一取出字母c再判斷
            if c=='*': ans.pop() # 遇到星號,吐掉1個字母
            else: ans.append(c) # 把不是星號的字母,塞進去
        return ''.join(ans) # 用單單.join() 成字串
