#======================================================================
# 6.2절
#======================================================================
class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link			        

class LinkedStack :
    def __init__( self ):	
        self.top = None	    

    def isEmpty( self ): return self.top == None
    def clear( self ): self.top = None		    
    def push( self, item ):	                	
        n = Node(item, self.top)	        	
        self.top = n			

    def pop( self ):			
        if not self.isEmpty():	
            n = self.top		
            self.top = n.link	
            return n.data		

    def peek( self ):			
        if not self.isEmpty():	
            return self.top.data


    def size( self ):			
        node = self.top			
        count = 0
        while not node == None :
            node = node.link	
            count += 1			
        return count			

    def display( self, msg='LinkedStack:'): 
        print(msg, end='')		
        node = self.top			
        while not node == None :	 	
            print(node.data, end=' ')	
            node = node.link		    
        print()

odd = LinkedStack()		
even = LinkedStack()	
for i in range(10):		    	    
    if i%2 == 0 : even.push(i) 		
    else : odd.push(i)			    

even.display(' 스택 even push 5회: ')
odd.display (' 스택 odd  push 5회: ')	
print(' 스택 even     peek: ', even.peek())
print(' 스택 odd      peek: ', odd.peek())	
for _ in range(2) : even.pop()		
for _ in range(3) : odd.pop()		
even.display(' 스택 even  pop 2회: ')
odd.display (' 스택 odd   pop 3회: ')

#======================================================================
# 6.3절
#======================================================================
class LinkedList:			
    def __init__( self ):			
        self.head = None			

    def isEmpty( self ): return self.head == None	
    def clear( self ) : self.head = None		    

    def size( self ):			
        node = self.head		
        count = 0
        while not node == None :
            node = node.link	
            count += 1			
        return count			

    def display( self, msg='LinkedList:'): 
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print(node.data, end=' ')	
            node = node.link		    
        print()

    def getNode(self, pos) :		     
        if pos < 0 : return None
        node = self.head		     
        while pos > 0 and node != None :
            node = node.link		     
            pos -= 1			         
        return node	

    def getEntry(self, pos) :		    
        node = self.getNode(pos)		
        if node == None : return None	
        else : return node.data		    

    def replace(self, pos, elem) :	    
        node = self.getNode(pos)		
        if node != None: node.data = elem	

    def find(self, data) :		    
        node = self.head
        while node is not None:		
            if node.data == data : return node	
            node = node.link
        return node			

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)		    
        if before == None :         		    
            self.head = Node(elem, self.head)	
        else :					                
            node = Node(elem, before.link)		
            before.link = node		


    def delete(self, pos) :
        before = self.getNode(pos-1)		
        if before == None :         		
            if self.head is not None :		
                self.head = self.head.link	
        elif before.link != None :		    
            before.link = before.link.link	


s = LinkedList()
s.display('단순연결리스트로 구현한 리스트(초기상태):')
s.insert(0, 10);	s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);	s.insert(2, 50)
s.display("단순연결리스트로 구현한 리스트(삽입x5): ")
#s.sort()
#s.display("단순연결리스트로 구현한 리스트(정렬후): ")
s.replace(2, 90)
s.display("단순연결리스트로 구현한 리스트(교체x1): ")
s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("단순연결리스트로 구현한 리스트(삭제x3): ")
#lst = [1, 2, 3]
#s.merge(lst)
#s.display("단순연결리스트로 구현한 리스트(병합+3): ")
s.clear()
s.display("단순연결리스트로 구현한 리스트(정리후): ")


#======================================================================
# 6.4절
#======================================================================
class CircularLinkedQueue:
    def __init__( self ):		
        self.tail = None			

    def isEmpty( self ): return self.tail == None 
    def clear( self ): self.tail = None		
    def peek( self ):				        
        if not self.isEmpty():			    
            return self.tail.link.data		

    def enqueue( self, item ):	
        node = Node(item, None)	
        if self.isEmpty() :		
           node.link = node		
           self.tail = node		
        else :				           
            node.link = self.tail.link	
            self.tail.link = node	   
            self.tail = node		   

    def dequeue( self ):
        if not self.isEmpty():
            data = self.tail.link.data		   
            if self.tail.link == self.tail :
                self.tail = None		               
            else:			                	
                self.tail.link = self.tail.link.link
            return data			

    def size( self ):
        if self.isEmpty() : return 0	
        else :				            
            count = 1			        
            node = self.tail.link   	
            while not node == self.tail:
                node = node.link        
                count += 1		        
            return count		        

    def display( self, msg='CircularLinkedQueue:' ):
        print(msg, end='')
        if not self.isEmpty() :
            node = self.tail.link		    
            while not node == self.tail :	
                print(node.data, end=' ')	
                node = node.link		    
            print(node.data, end=' ')		
        print()					            


q = CircularLinkedQueue()
for i in range(8): q.enqueue(i)		
q.display()			            	
for i in range(5): q.dequeue();		
q.display()
for i in range(8,14): q.enqueue(i)	
q.display()

#======================================================================
# 6.5절
#======================================================================
class DNode:				
    def __init__ (self, elem, prev = None, next = None):
        self.data = elem 
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__( self ):	
        self.front = None	
        self.rear = None

    def isEmpty( self ): return self.front == None		
    def clear( self ): self.front = self.front = None	

    def size( self ):			
        node = self.front			
        count = 0
        while not node == None :
            node = node.next	
            count += 1			
        return count			

    def display( self, msg='LinkedDeque:'): 
        print(msg, end='')		
        node = self.front			
        while not node == None :	 	
            print(node.data, end=' ')	
            node = node.next		    
        print()

    def addFront( self, item ):
        node = DNode(item, None, self.front)
        if( self.isEmpty()):				
            self.front = self.rear = node	
        else :								
            self.front.prev = node			
            self.front = node				


    def addRear( self, item ):
        node = DNode(item, self.rear, None)	
        if( self.isEmpty()):				
            self.front = self.rear = node	
        else :								
            self.rear.next = node			
            self.rear = node				

    def deleteFront( self ):
        if not self.isEmpty():
            data = self.front.data			
            self.front = self.front.next	
            if self.front==None :			
                self.rear = None			
            else:
                self.front.prev = None		
            return data						

    def deleteRear( self ):
        if not self.isEmpty():
            data = self.rear.data			
            self.rear = self.rear.prev		
            if self.rear==None :			
                self.front = None			
            else:
                self.rear.next = None		
            return data						



dq = DoublyLinkedDeque()		 			
for i in range(9):			        
	if i%2==0 : dq.addRear(i)		
	else : dq.addFront(i)		    
dq.display()				        
for i in range(2): dq.deleteFront()	
for i in range(3): dq.deleteRear()	
dq.display()
for i in range(9,14): dq.addFront(i)
dq.display()

#----------------------------------------------------------------------
