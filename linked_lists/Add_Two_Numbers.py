# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
    carry = 0
    current = None
    head = None

    while l1 or l2 or carry:
        sum = carry

        if l1:
            sum += l1.val
        if l2:
            sum += l2.val
        
        digit = sum % 10
        carry = sum // 10

        newNode = ListNode(digit)
        if head is None:
            head = newNode
            current = newNode
        else:
            current.next = newNode # type: ignore
            current = newNode

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return head


