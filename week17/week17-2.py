# week17-2.py 學習計畫 Trie 第2題
 # LeetCode 1268. Search Suggestions System
 # searchWord 每次輸入1個字母,找到對應的products前3名
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() # 把所有產品名字,照字母順序排序,以便插入時,字母小的在前面
        root = defaultdict(list) # trie的資料結構的1個node,當樹根
        for product in products: # 很多產品products逐一挑出1個產品product
            now = root # 每個產品,都要逐字母 在trie
            for c in product: # 逐字母往下滑(邊滑邊建資料結構)
               if c not in now: now[c] = defaultdict(list) # 缺node就補
               now = now[c] # 再往下滑
            now['*'] = product # 結尾打個「星星」產品名,直接放在裡面
        now = root # 現在要再滑一次,從root往下滑
        ans = [] # 把最接近的前3筆product產品,塞到 ans 裡
        for c in searchWord: # 逐個字母,每個字母輸入後,累積的 prefix要找到前3筆best
            best = [] # 最好的前3筆產品
            if c not in now: # 根本沒有這個字母的圈圈node,後面都沒有答案了
               noResult = len(searchWord) - len(ans) # 還欠幾筆答案
               return ans + [[] for i in range(noResult)]
            now = now[c] # 往下滑
            def helper(now):
                if '*' in now: best.append(now['*']) # 看到有字,就先塞答案
                for c in now: # 接下來逐個字母處理
                    if len(best)<3 and c != '*':
                        helper(now[c]) # 函式呼叫函式
            helper(now) # 函式呼叫函式
            ans.append(best)
        return ans
