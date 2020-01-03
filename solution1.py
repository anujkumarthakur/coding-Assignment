# Q1.Reverse singly linked list, with O(n) space complexity and O(n) time complexity
'''
|------|   |-----|   |-----|
| head |   |Prev |   |Curr |
|------|   |-----|   |-----|
   
  Node           Node            Node            Node            Node            Node            Node
|---|---|       |---|---|       |---|---|       |---|---|       |---|---|       |---|---|       |---|---|       
| D | N |---->  | D | N |  -->  | D | N |---->  | D | N |  -->  | D | N |  -->  | D | N |---->  | D | N |  
|   |   |       |   |   |       |   |   |       |   |   |       |   |   |       |   |   |       |   |   |        
---------       ---------       ---------       ---------       ---------       ---------       ---------
'''
                
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): 
        self.head = None 
    #push function to store data in node
    def push(self, p_data):
        n_node = Node(p_data)
        n_node.next = self.head
        self.head = n_node
    
    #reverse function to reverse a single linked list 
    #it is retrive one by one value in  the same way like that
    # 5-->1-->2-->3-->4 left to right(BigO(n))
    # 4<--3<--2<--1<--<5 right to left(BigO(n))
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev 
 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ =="__main__":
    obj = LinkedList()
    #Dynamic Memory Consuming on Run Time
    while(True):
        inp = int(input("Enter data for new node:"))
        if(inp > 0):
            obj.push(inp)
        else:
            break
    
    obj.printList() 
    obj.reverse() 
    obj.printList()  

