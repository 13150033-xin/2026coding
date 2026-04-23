# week09-6.py 學習計畫Linked List 第2題
# LeetCode 328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = [] # 先轉成陣列a
        while head: # 逐一將Link List的值,放入陣列a
            a.append( head.val )
            head = head.next # 記得換下一筆

        N = len(a) # 陣列的大小
        now = ans = ListNode() # 答案,有個 Node 右邊會塞真的 Nodes
        for i in range(0, N, 2): # 偶數堆
            now.next = ListNode( a[i] ) # 逐一塞進去
            now = now.next # 串接下一個
        for i in range(1, N, 2): # 奇數堆
            now.next = ListNode( a[i] ) # 逐一塞進去
            now = now.next # 串接下一個
        return ans.next
