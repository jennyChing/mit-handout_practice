class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tort = head
        hare = head
        while hare!=None and hare.next!= None:
            tort = tort.next
            hare = hare.next.next
            if tort == hare:
# set hare back to starting point, the nearest meeting point is the start of the cycle
                hare = head
                while tort!=hare:
                    tort = tort.next
                    hare = hare.next
                return tort
        return False
if __name__ == "__main__":
# use __init__ to construct a object called linked_list
    linked_list = ListNode(5)
    # use ListNode constructor to create a new node in linked list
    linked_list.next = ListNode(6)
    linked_list.next.next = ListNode(7)
    linked_list.next.next.next = linked_list.next.next # point back to existing value
# call the Solution function with no input value
    sol = Solution()#
    # find the start of the cycle
    print(sol.hasCycle(linked_list).val)
    #assert sol.hasCycle(linked_list)==False, "wrong output"
