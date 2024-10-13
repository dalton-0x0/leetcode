"""
There is a singly-linked list head and, we want to delete a node in it.
You are given the node to be deleted node. You will not be given access to the first node of head.
All the values of the linked list are unique, and it is guaranteed that the given node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before node should be in the same order.
- All the values after node should be in the same order.
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def deleteNode(node):
    # Copy the value of the next node to the current node
    node.val = node.next.val
    # Bypass the next node
    node.next = node.next.next


def printLinkedList(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


# Helper function to create a linked list from a list and return both head and the node at the given index
def createLinkedList(values, index_to_return):
    head = ListNode(values[0])
    current = head
    node_to_return = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == index_to_return:
            node_to_return = current

    return head, node_to_return


# Test Case 1
test_head, node_to_delete = createLinkedList([4, 5, 1, 9], 1)
print("Original list:")
printLinkedList(test_head)

deleteNode(node_to_delete)
print("List after deletion:")
printLinkedList(test_head)

# Test Case 2
test_head, node_to_delete = createLinkedList([1, 2, 3, 4, 5], 2)
print("Original list:")
printLinkedList(test_head)

deleteNode(node_to_delete)
print("List after deletion:")
printLinkedList(test_head)

