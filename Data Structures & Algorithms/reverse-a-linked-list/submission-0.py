# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        prevNode = None
        bufferNode = None
        while curNode != None:

            bufferNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = bufferNode
            # if print(f"current Node: {curNode.val}")
            # if curNode.next != None:
            #     print(f"current Node next: {curNode.next.val}")
            # else:
            #     print(f"current Node next: None")
            # if prevNode != None: 
            #     print(f"prev Node: {prevNode.val}")
            # else:
            #     print("prev Node: None")
            # if prevNode.next != None:
            #     print(f"prev Node next: {prevNode.next.val}")
            # else:
            #     print(f"prev Node next: None")

            # A -> B -> C
            # A <- B x C

        return prevNode
        