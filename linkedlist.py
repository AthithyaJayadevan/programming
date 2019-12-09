class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.val = data  # Assign data
        self.next = None  # Initialize next as null


def k_recursive_last_element(head, k):
    if head == None:
        return 0
    #print('head' + str(head.val))
    ind = k_recursive_last_element(head.next, k)+1
    if ind == k:
        print('Node found ' + str(head.val))
    return ind

def common_index(l1, l2):
    if l1 is None or l2 is None:
        return None
    t1 = l1
    t2 = l2
    length1=0
    length2=0
    while t1 is not None:
        t1 = t1.next
        length1+=1
    while t2 is not None:
        t2 = t2.next
        length2+=1
    if t1 != t2 :
         return None

    great = l1 if length1 > length2 else l2
    small = l1 if length1 < length2 else l2
    diff = abs(length1 - length2)
    while diff > 0:
        great = great.next
        diff-=1

    while small != great:
        great = great.next
        small = small.next

    return great.val


def palindrome_checker(l1):
    one=l1
    two=l1
    while two and two.next:
        one = one.next
        two = two.next.next

    stack =[]

    while one:
        stack.append(one.val)
        one= one.next
    while stack:
        elem = stack.pop()
        if l1.val != elem:
            return False
        l1= l1.next
    return True

# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def add_two_linked_list(self, l1, l2):
        prev = None
        carry = 0
        temp = None

        while l1 is not None or l2 is not None:
            first_data = l1.val if l1 is not None else 0
            second_data = l2.val if l2 is not None else 0

            s = carry + first_data + second_data

            carry = 1 if s >= 10 else 0
            s = s%10 if s >= 10 else s
            temp = Node(s)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            temp.next = Node(carry)


    def remove_duplicates(self):
        t=self.head
        elements=[]
        while t.next:
            ne = t.next
            if ne.val in elements:
                t.next= ne.next
            else:
                elements.append(ne.val)
            t=t.next


    def k_last_element(self, k):
        t=self.head
        length=0
        while t:
            length+=1
            t=t.next

        pos = length-k+1
        count=1

        t=self.head
        while t:
            if count == pos:
                return t.val
            count+=1
            t=t.next
        return 'Not Found'



    def del_middle_node(self):
        t=self.head
        one=t
        two=t
        prev=Node(None)
        while two and two.next:
            prev = one
            one = one.next
            two = two.next.next
        ssec=one.next
        prev.next=ssec



    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next

# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    llist1 = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    sam = Node(3)
    four = Node(1)
    five = Node(1)
    llist.head.next = second
    second.next = third
    third.next=sam
    sam.next = four
    four.next = five

    llist1.head = Node(1)
    second2 = Node(7)
    llist1.head.next = second2
    second2.next = sam

    print(common_index(llist1.head, llist.head))