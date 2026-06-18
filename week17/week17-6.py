# week17-6.py 學習計畫  Heap / Priority Queue 第4題
# LeetCode 2462. Total Cost to Hire K Workers
# costs[i] 可聘用第i個人,每次從「最左 or 最右」 candidates的數量裡,挑「最便宜」的人,共挑k人
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs) # 有N個工人
        if candidates * 2 + k > N: # 狀況1:最後一定全部都能挑,那就挑最小的K個人
            heapify(costs)
            ans = 0
            for i in range(k): ans += heappop(costs) # 要挑出k個工人
            return ans
        # 狀況2:兩頭不會合併在一起,那我們就準備2堆heap
        heap1, heap2 = [], [] # 把heap都長大成k個
        for i in range(candidates):
            heappush(heap1, costs[i]) # 左邊的候選人
            heappush(heap2, costs[N-1-i]) # 右邊的候選人
        ans = 0
        left, right = candidates, N-candidates-1
        for i in range(k): # 要挑出k個工人
            if heap1[0] <= heap2[0]: # 兩邊最小的,決定挑左邊的
               ans += heappop(heap1) # 挑左邊的
               heappush(heap1, costs[left]);left += 1 # 左邊再補1位
            else: # 右邊小
               ans += heappop(heap2)# 挑右邊的
               heappush(heap2, costs[right]);right -= 1  # 右邊再補1位
        return ans
