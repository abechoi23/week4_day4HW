from linkedList import Node, LinkedList

def sorting_decorator(func):

    def inner(alist):
        alist.sort()

        return func(alist)

    return inner

@sorting_decorator
def convert_to_linked_list(alist):
    head_node = Node(alist[0])
    linkedList = LinkedList(head_node)
    for i in range(1, len(alist)):
        linkedList.insert_after(alist[i])
    linkedList.print_nodes()
    return linkedList

convert_to_linked_list([4,1,2,4,12,532,-2,10])