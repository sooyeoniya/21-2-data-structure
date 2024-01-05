#======================================================================
# 5.2절
#======================================================================
items = [ ]

def isEmpty():
    return len(items) == 0	

def enqueue(item):
    items.append(item)		

def dequeue():
    if not isEmpty():		
        return items.pop(0)	

def peek():			        
    if not isEmpty(): return items[-1]

#----------------------------------------------------------------------
MAX_QSIZE = 10				    
class CircularQueue :
    def __init__( self ) :		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty( self ) : return self.front == self.rear
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE
    def clear( self ) : self.front = self.rear

    def enqueue( self, item ):
        if not self.isFull():			            
            self.rear = (self.rear+1)% MAX_QSIZE	
            self.items[self.rear] = item		    

    def dequeue( self ):
        if not self.isEmpty():			            
            self.front = (self.front+1)% MAX_QSIZE	
            return self.items[self.front]	        

    def peek( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size( self ) :
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]		
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)


q = CircularQueue()			       
for i in range(8): q.enqueue(i)		
q.display()			            	
for i in range(5): q.dequeue();		
q.display()
for i in range(8,14): q.enqueue(i)	
q.display()


#======================================================================
# 5.3절
#======================================================================
def isValidPos(x, y) :		
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False		
    else :			        
        return map[y][x] == '0' or map[y][x] == 'x'

def BFS() :			    	
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS: ')			

    while not que.isEmpty(): 
        here = que.dequeue()
        print(here, end='->')
        x,y = here
        if (map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : que.enqueue((x, y - 1))	
            if isValidPos(x, y + 1) : que.enqueue((x, y + 1))	
            if isValidPos(x - 1, y) : que.enqueue((x - 1, y))	
            if isValidPos(x + 1, y) : que.enqueue((x + 1, y))	
    return False

map = [   [ '1', '1', '1', '1', '1', '1' ],
	    [ 'e', '0', '1', '0', '0', '1' ],
	    [ '1', '0', '0', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '0', 'x' ],
	    [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6
result = BFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')

#----------------------------------------------------------------------
import queue 			   
Q = queue.Queue(maxsize=20)

for v in range(1, 10) : 
    Q.put(v) 
print("큐의 내용: ", end='')  
for _ in range(1, 10) : 
    print(Q.get(), end=' ')
print()


#======================================================================
# 5.5절
#======================================================================
class CircularDeque(CircularQueue) :	          
    def __init__( self ) :		                  
        super().__init__()		                  

    def addRear( self, item ): self.enqueue(item )
    def deleteFront( self ): return self.dequeue()
    def getFront( self ): return self.peek()		
   
    def addFront( self, item ):			          
        if not self.isFull():
            self.items[self.front] = item        
            self.front = self.front - 1		      
            if self.front < 0 : self.front = MAX_QSIZE - 1

    def deleteRear( self ):			      
        if not self.isEmpty():
            item = self.items[self.rear];
            self.rear = self.rear - 1		
            if self.rear < 0 : self.rear = MAX_QSIZE - 1
            return item			     

    def getRear( self ):			 
        return self.items[self.rear]
        

dq = CircularDeque()		        
for i in range(9):			        
	if i%2==0 : dq.addRear(i)		
	else : dq.addFront(i)		    
dq.display()				        
for i in range(2): dq.deleteFront()	
for i in range(3): dq.deleteRear()	
dq.display()
for i in range(9,14): dq.addFront(i)
dq.display()



#======================================================================
# 5.6절
#======================================================================
class PriorityQueue :
    def __init__( self ):					
        self.items = []						

    def isEmpty( self ):					
        return len( self.items ) == 0
    def size( self ): return len(self.items)
    def clear( self ): self.items = []		

    def enqueue( self, item ):				
        self.items.append( item )			

    def findMaxIndex( self ):				
        if self.isEmpty(): return None
        else:
            highest = 0						
            for i in range(1, self.size()) :
                if self.items[i] > self.items[highest] :
                    highest = i	
            return highest		


    def dequeue( self ):		
        highest = self.findMaxIndex()		
        if highest is not None :
            return self.items.pop(highest)	

    def peek( self ):				
        highest = findMaxIndex()	
        if highest is not None :
            return self.items[highest]	

q = PriorityQueue()
q.enqueue( 34 )
q.enqueue( 18 )
q.enqueue( 27 )
q.enqueue( 45 )
q.enqueue( 15 )

print("PQueue:", q.items)
while not q.isEmpty() :
    print("Max Priority = ", q.dequeue() )


#======================================================================
# 5.7절
#======================================================================

import math				
(ox,oy) = (5, 4)		
def dist(x,y) :			 
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)	



    def findMaxIndex( self ):		
        if self.isEmpty(): return None
        else:
            highest = 0				
            for i in range(1, self.size()) :	
                if self.items[i][2] > self.items[highest][2] :
                    highest = i		
            return highest			



def MySmartSearch() :				
    q = PriorityQueue()				
    q.enqueue((0,1,-dist(0,1)))		
    print('PQueue: ')

    while not q.isEmpty(): 
        here = q.dequeue()
        print(here[0:2], end='->')	
        x,y,_ = here				
        if (map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : q.enqueue((x,y-1, -dist(x,y-1)))
            if isValidPos(x, y + 1) : q.enqueue((x,y+1, -dist(x,y+1)))
            if isValidPos(x - 1, y) : q.enqueue((x-1,y, -dist(x-1,y)))
            if isValidPos(x + 1, y) : q.enqueue((x+1,y, -dist(x+1,y)))
        print('우선순위큐: ', q.items)
    return False