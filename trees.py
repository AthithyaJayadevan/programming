class Node:
    def __init__(self, data):
        self.val = data
        self.left=None
        self.right = None


class LinkedList:
    next = None
    val = None

    def __init__(self, val):
        self.val = val

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

class Tree:
    def __init__(self, node):
        self.root = node




def insert_nodes(root, node):
    if root:
        val = node.val
        if val < root.val:
            if root.left is None:
                root.left = node
            else:
                insert_nodes(root.left, node)
        if val > root.val:
            if root.right is None:
                root.right = node
            else:
                insert_nodes(root.right, node)


def sorted_array_to_BST(a):
    if not a:
        return None
    middle = (len(a))//2
    root = Node(a[middle])
    root.right = sorted_array_to_BST(a[middle+1:])
    root.left = sorted_array_to_BST(a[:middle])
    return root


def insert_in_order(root, d):
    if root.val < d:
        if root.right is None:
            root.right = Node(d)
        else:
            insert_in_order(root.right, d)
    else:
        if root.left is None:
            root.left = Node(d)
        else:
            insert_in_order(root.left, d)
    return root


def range_sum_BST(root, range1, range2):
    if root is None:
        return 0
    sum1=0
    if root.val >= range1 and root.val <= range2:
        sum1+= root.val
    if root.left:
        sum1+= range_sum_BST(root.left, range1, range2)
    if root.right:
        sum1+=range_sum_BST(root.right, range1, range2)
    return sum1

def univalued_binary_tree(root):
    if root is None:
        return True
    val = root.val
    stack=[root]

    while stack:
        elem = stack.pop()
        if elem.val != val:
            return False
        if elem.left:
            stack.append(elem.left)
        if elem.right:
            stack.append(elem.right)

    return True


def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return max(height(root.left), height(root.right)) + 1


def is_balanced(root):
    if root:
        left = height(root.left)
        right = height(root.right)

        if abs(left-right) >1:
            return False
        else:
            is_balanced(root.left)
            is_balanced(root.right)

        return True


def is_a_bst(root):
    if root is None:
        return True

    left = root.left
    right = root.right

    if left and left.val > root.val:
        return False
    if right and right.val < root.val:
        return False

    is_a_bst(root.left)
    is_a_bst(root.right)

    return True


def left_most_child(node):
    if node is None:
        return node
    while node.left:
        node = node.left

    return node


def in_order_sucessor(node):
    if node is None:
        return None

    if node.right is None:
        return left_most_child(node)




def linked_list_of_level_nodes(root, level, lists):
    if root is None:
        return None
    if level not in lists.keys():
        lists[level] = root.val
    else:
        lists[level].add(root.val)
        if level == 1:
            return lists
    if root.left:
        lists = linked_list_of_level_nodes(root.left, level-1, lists)
    if root.right:
        lists = linked_list_of_level_nodes(root.right, level-1, lists)

    return lists



def subtree(t1, t2):
    if t1 is None or t2 is None:
        return True

    if t1.val == t2.val and matchsubtree(t1, t2):
        return True

    return subtree(t1.left, t2) or subtree(t1.right, t2)

def matchsubtree(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    elif t1.val != t2.val:
        return False
    else:
        return matchsubtree(t1.left, t2.left) and matchsubtree(t1.right, t2.right)





def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)





r = Node(50)
insert_nodes(r,Node(30))
insert_nodes(r,Node(20))
insert_nodes(r,Node(40))
insert_nodes(r,Node(70))
insert_nodes(r,Node(60))
insert_nodes(r,Node(80))
arr = [2,2,2,2,2,2,2,2,2,2]

r1 = sorted_array_to_BST(arr)
# print('Inorder')
# inorder(r1)
# print('preorder')
# preorder(r1)
# print('postorder')
# postorder(r1)

print(is_a_bst(r))