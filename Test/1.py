class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if not l1 and not l2:
            return
        res = []
        q1, q2 = l1, l2
        while q1:
            res.append(q1)
            q1 = q1.next    
        while q2:
            res.append(q2) 
            q2 =q2.next         
        res = sorted(res, key=lambda x:x.val)
        return [i.val for i in res]

l1=[1,2,4]
l2=[1,3,4]
s=Solution()
s.mergeTwoLists(l1,l2)


print(s.mergeTwoLists(l1,l2))