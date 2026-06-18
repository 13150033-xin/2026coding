# week17-1.py 學習計畫 Trie 第1題
 # LeetCode 208. Implement Trie (Prefix Tree)
 # 建出 Trie 的資料結構,要實作insert() search() startWidth()
class Trie:

    def __init__(self):
        self.root = defaultdict(list) # 樹的 root

    def insert(self, word: str) -> None:
        now = self.root # 一開始now 在最上面的root node
        for c in word: # 逐字母加入Trie 資料結構
            if c not in now: now[c] = defaultdict(list)
            now = now[c] # 走到下一個圓圈圈
        now['*'] = defaultdict(list) # 字的結尾,打星星

    def search(self, word: str) -> bool:
        now = self.root # 一開始now 在最上面的root node
        for c in word:#逐字母加入Trie 資料結構
            if c not in now: return False # 沒有這個字母的圈圈,失敗
            now = now[c] # 可以往下滑
        return '*' in now # 最後的圓圈,有沒有字的結尾的星星

    def startsWith(self, prefix: str) -> bool:
        now = self.root # 一開始now 在最上面的root node
        for c in prefix: # 逐字母加入Trie 資料結構
            if c not in now: return False # 沒有這個字母的圈圈,失敗
            now = now[c] # 可以往下滑
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
