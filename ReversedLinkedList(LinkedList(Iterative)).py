#Definition for singly-linked list.
 
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1, p2 = None, head

        while p2: #p2!=null
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        return p1 #the entire linked list (object) is stored in the head since it has the address of all the notes head -> node 1 -> node 2 ...



def create_linkedlist(lst: list) -> ListNode:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for num in lst[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

list_vals = [1, 2, 3, 4, 5]
head = create_linkedlist(list_vals)

# To verify, let's print the linked list
def print_linkedlist(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

print_linkedlist(head)

# Now let's test the reverseList function
solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed linked list:")
print_linkedlist(reversed_head)
