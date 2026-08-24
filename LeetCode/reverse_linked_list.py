class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    # using pointers to reverse the node's pointer as we go thru the list
    L,R = None, head

    while R:
        temp = R.next # storing the address of the next node
        R.next = L # reverse the node's pointer to the opposite way
        L = R # shift the L to the node where R is at
        R = temp # reconnect with the rest of the list
    return L

link1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
result1 = reverseList(link1)

curr = result1
while curr:
    print(curr.val)
    curr = curr.next