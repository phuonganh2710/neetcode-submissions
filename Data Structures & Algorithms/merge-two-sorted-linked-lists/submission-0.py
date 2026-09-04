# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        # print(ptr1)
        ptr2 = list2
        # print(ptr2)
        mainPtr = ListNode()
        anchor = mainPtr
        

        while ptr1 != None or ptr2 != None:
            # print(f"list1: {ptr1.val}")
            # print(f"list2: {ptr2.val}")
            if ptr1 == None:
                mainPtr.next = ptr2
                ptr2 = ptr2.next
                mainPtr = mainPtr.next
                continue
            
            if ptr2 == None:
                mainPtr.next = ptr1
                ptr1 = ptr1.next
                mainPtr = mainPtr.next
                continue
            
            if ptr1.val <= ptr2.val:
                mainPtr.next = ptr1
                ptr1 = ptr1.next
            else: 
                mainPtr.next = ptr2
                ptr2 = ptr2.next
            
            mainPtr = mainPtr.next

        return anchor.next

