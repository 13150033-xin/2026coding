# week17-4.py 學習計畫 Array/Strin 第9題
# LeetCode 443. String Compression
class Solution:
    def compress(self, chars: List[str]) -> int:
        # 字串壓縮,變成一堆字母+數字,結果要放在chars陣列裡
        N = 1 # 字串的長度
        prev, combo = chars[0],0 # 前一個字母重覆combo 幾次
        for c in chars: # 逐字母取出來
            if c == prev: combo += 1 # 字母相同  combo += 1
            else: # 字母不同,糟!
                if combo > 1: # 有很多重覆的字母,就要塞數字
                    for c2 in str(combo): # 把整數,變字串
                        chars[N] = c2 # 要塞數字
                        N += 1
                prev, combo = c, 1 # 新的字母、新的開始
                chars[N] = c
                N += 1
        if combo > 1: # 有很多重覆的字母,就要塞數字
            for c2 in str(combo): # 把整數,變字串
                chars[N] = c2 # 要塞數字
                N += 1
        return N # 字串的長度
