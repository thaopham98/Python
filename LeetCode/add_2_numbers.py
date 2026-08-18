"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = []
        remain = 0
        carry = 0 
        while l1 or l2:

            # sum = l1.val + l2.val
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 

            total = val1 + val2 + carry
            carry = total//10
            remain = total%10

            # print(f"sum: {sum}, remain: {remain}, carry: {carry}")
            l3.append(remain)

            # print(l3.val)

            if l1:
                l1 = l1.next

            if l2: 
                l2 = l2.next
            
            # l3 = l3.next

        if carry:
            l3.append(carry)
        return l3

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    
class Solution3:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(0) # []
            current = dummy
            carry = 0 
            while l1 or l2:

                val1 = l1.val if l1 else 0
                val2 = l2.val if l2 else 0 

                total = val1 + val2 + carry
                carry = total//10
                remain = total%10

                newNode =  ListNode(remain) # create a new node from the resulst, this is like newNode.val
                current.next = newNode # add the new node as the next node. dummmy(0)->newNode(remain)
                current = newNode # move the current pointer to the new node

                if l1:
                    l1 = l1.next

                if l2: 
                    l2 = l2.next
                    
            if carry:
                newNode =  ListNode(carry) # create a new node from the resulst, this is like newNode.val
                # current.next = newNode # add the new node as the next node. dummmy(0)->newNode(carry)
                # current = newNode # move the current pointer to the new node

            return dummy.next


## ------------------- TEST CASES -------------------
# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
# l4 = [9,9,9,9,9,9,9]
# l5 = [9,9,9,9]
# # res = 8, 9, 9, 9, 0, 0, 1
l4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))


## ------------------- METHOD 1 -------------------
sol1 = Solution1()
answer1 = sol1.addTwoNumbers(l1, l2)
print(f"ANSWER 1: {answer1}")
answer2 = sol1.addTwoNumbers(l4, l1)
print(f'ANSWER 2: {answer2}')


## ------------------- METHOD 3 -------------------
sol3 = Solution3()
answer3 = sol3.addTwoNumbers(l4, l5)
result = []
current = answer3

while current:
    result.append(current.val)
    current = current.next

print(f"ANSWER 3: {result}")