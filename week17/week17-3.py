# week17-3.py 學習計畫 Array/Strin 第5題
# LeetCode 345. Reverse Vowels of a String
# 將「母音」的順序「反過來」
class Solution:
    def reverseVowels(self, s: str) -> str:
        V = "aeiouAEIOU" # 字串(若用 Python 的集合,會更快)
        stack = [] # 可以倒過來的資料結構
        for c in s: # 逐字母分析
            if c in V: stack.append(c) # 遇到母音,就抄下來

        ans = ""
        for c in s:  # 再逐字母處理一下,塞答案
            if c in V: ans += stack.pop() #母音「倒過來」塞
            else: ans += c # 子音直接塞
        return ans
