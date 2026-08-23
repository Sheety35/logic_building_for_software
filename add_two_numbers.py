# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversed(self, linked_list):
        prev = None
        curr = linked_list

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev

    def linked_list_to_int(self, l1):
        result = 0 
        while l1:
            result = (result * 10) + l1.val
            l1 = l1.next
        return result

    def int_to_linked_list(self, int_num):
        temp = str(int_num)

        head = ListNode(int(temp[0]))
        current = head

        for digit in temp[1:]:
            current.next = ListNode(int(digit))
            current = current.next

        current = self.reversed(head)

        return current

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reversed(l1)
        l2 = self.reversed(l2)

        l1_val = self.linked_list_to_int(l1)
        l2_val = self.linked_list_to_int(l2)

        summ = l1_val + l2_val

        summ = self.int_to_linked_list(summ)

        return summ
        