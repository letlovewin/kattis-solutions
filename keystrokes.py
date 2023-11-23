#A naive solution here would be to make a list of characters and add or delete them according to instructions. This would be fine if there were no backspace command.
#With there being a backspace command, removing from the middle or beginning of the list can be troublesome, since that would be an O(n) operation. A doubly linked list would make all of these operations O(1).
#The most expensive operation here is printing the result.

class Node:
    def __init__(self,val='',back=None,next=None):
        self.back = back
        self.next = next
        self.val = val

def solve():
    s = input()
    cur = None
    for i in s:
        if cur==None and not i in 'LRB':
            d1 = Node()
            d2 = Node()
            n = Node(i)
            n.back = d1
            n.next = d2
            d1.next = n
            d2.back = n
            cur = n
        elif i=='L':
            cur = cur.back
        elif i=='R':
            cur = cur.next
        elif i=='B' and cur.val != '':
            tempback = cur.back
            tempforward = cur.next
            cur.back = None
            cur.next = None
            tempback.next = tempforward
            tempforward.back = tempback
            cur = tempback
        else:
            if cur.next!=None:
                n = Node(i)
                n.back = cur
                n.next = cur.next
                cur.next = n
                n.next.back = n
                cur = n
    while cur.back != None:
        cur = cur.back
    while cur != None:
        print(cur.val,end='')
        cur = cur.next
    print("")
solve()

#GrayBBBBgraysoLLisRRawesome
