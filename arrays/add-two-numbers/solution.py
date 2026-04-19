# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nodes = ListNode(0)
        carry = 0
        aux = nodes

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            result = a + b + carry
            carry = result // 10
            digit = result % 10

            aux.next = ListNode(digit)
            aux = aux.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return nodes.next