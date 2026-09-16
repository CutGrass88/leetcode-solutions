class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    head = None
    current = None
    while list1 or list2:
        if list1 is None and list2:
            newNode = ListNode(list2.val)
            list2 = list2.next
        elif list2 is None and list1:
            newNode = ListNode(list1.val)
            list1 = list1.next
        else:

            if (list1.val <= list2.val):
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
        
        if head is None:
            head = newNode
            current = newNode
        else:
            current.next = newNode # type: ignore
            current = current.next # type: ignore
    return head

