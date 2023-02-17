class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert_before(self, value, target_value=None):
        """
        Insert a new node with the provided value before the node
        with the same value as target_value.
        If there is not target_value, insert the new node to
        the front of the list. 
        """
        new_node = Node(value)
        # Check if there is not a target_value
        if not target_value:
            
        #If there's not a target value, check if there is a head node
                
            if self.head:
            #If there is a head, set the next_node property
            #Of our new node, so that we do not break our chain
            #when we update the head to be our new_node
                new_node.next_node = self.head
                
            #Update the head to be my new node    
            self.head = new_node

          #If there is a target value, find the node with that target value
        else:
            current_node = self.head
            prev_node = None

            #Loop through all of our nodes
            while current_node:

                #Check if current_node's value == the target value
                if current_node.value == target_value:
                    #Set the previous node's next_node attribute to the new node
                    prev_node.next_node = new_node
                    #set the new node's next_node attribute to the current_node
                    new_node.next_node = current_node
                    
                    break
                    
                prev_node = current_node
                current_node = current_node.next_node
        
        
    def remove(self,value):
        """
        Iterate through all of the nodes, until you find the node that has the value you're looking for. Once you find the node you're looking for set the next_node attribute for the previous node, to the node you found's next_node attribute. Effectively removing the node from the chain, as there is no longer any reference to the node.
        """

        current_node = self.head
        prev_node = None

        while current_node:
            if current_node.value == value:
                # If there is not a previous node, set the head to the current_node's next_node
                if not prev_node:
                    self.head = current_node.next_node

                else:
                    prev_node.next_node = current_node.next_node

                break

            prev_node = current_node
            current_node = current_node.next_node

        return False
    
    def insert_after(self,value,target_value=None):
        """
        Insert a new node with the provided value before the node
        with the same value as target_value.
        If there is not target_value, insert the new node to
        the front of the list. 
        """
        new_node = Node(value)
        
        # Check if there is not a target_value
        if not target_value:
            
            #If there's not a target value, check if there is a head node
            if self.head:
                #If there is a head, loop through your nodes to find the tail
                current_node = self.head
                
                #Stop once next_node is none, because then
                #current node is our tail.
                while current_node.next_node:
                    current_node = current_node.next_node
                    
                current_node.next_node = new_node
                
            else: 
                #Update the head to be my new node    
                self.head = new_node

        #If there is a target value, find the node with that target value
        else:
            current_node = self.head


            #Loop through all of our nodes
            while current_node:

                #Check if current_node's value == the target value
                if current_node.value == target_value:
                    
                    #Set the new_node's next node, to the current node's next node, to insert
                    #The new node before the next node
                    new_node.next_node = current_node.next_node
                    
                    #Set current_node's next node, to my new node, to insert it after the current_node
                    current_node.next_node = new_node
                    
                    break
                    
                current_node = current_node.next_node
    
    def contains(self,value):
        """
        Checks if a node with the provided value exists in my list.
        If it does, return true, if it doesn't return false.
        """
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            
            current_node = current_node.next_node

        return False

    
    def print_nodes(self):
        current_node = self.head
        
        #loop through each current node, until there are no more nodes
        #and print out the current node's value
        
        while current_node:
            print(current_node.value, end=' -> ')
            
            current_node = current_node.next_node
            
        print('None')

my_list = LinkedList()
my_list.insert_before(10)
my_list.print_nodes()
# print(my_list.head.value)
my_list.insert_before(20)
my_list.print_nodes()
my_list.insert_before(30, 10)
my_list.print_nodes()
my_list.insert_after(40)
my_list.print_nodes()
my_list.insert_after(50, 30)
my_list.print_nodes()

my_list.remove(20)
my_list.print_nodes()

print(my_list.contains(60))
print(my_list.contains(10))
# print('HELLO')

# while True:
#     user_input = input('Would you like to add or remove? ')

#     if user_input == 'add':
#         item_to_add = input('What do you want to add? ')
#         my_list.insert_before(item_to_add)
#     elif user_input == 'remove':
#         item_to_remove = input('What would you like to remove? ')
#         my_list.remove(item_to_remove)
    
#     my_list.print_nodes()