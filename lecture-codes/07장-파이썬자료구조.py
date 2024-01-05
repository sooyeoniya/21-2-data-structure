#======================================================================
# 7.2절
#======================================================================
def selection_sort(A) :						
    n = len(A)								
    for i in range(n-1) :					
        least = i;
        for j in range(i+1, n) :			
            if (A[j]<A[least]) :			
                least = j					
        A[i], A[least] = A[least], A[i]		
        printStep(A, i + 1);				

def printStep(arr, val) :					
    print("  Step %2d = " % val, end='')
    print(arr)

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
selection_sort(data)
print("Selection :", data)

#----------------------------------------------------------------------
def insertion_sort(A) :					
    n = len(A)
    for i in range(1, n) :				
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :		
            A[j + 1] = A[j]				
            j -= 1
        A[j + 1] = key					
        printStep(A, i)

#----------------------------------------------------------------------
def bubble_sort(A) :					
    n = len(A)
    for i in range(n-1, 0, -1) :		
        bChanged = False
        for j in range (i) :			
            if (A[j]>A[j+1]) :			
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True		

        if not bChanged: break;		
        printStep(A, n - i);		

#======================================================================
# 7.3절
#======================================================================
    def insert(self, elem) :                
        if elem in self.items : return      
        for idx in range(len(self.items)) : 
            if elem < self.items[idx] :     
                self.items.insert(idx, elem)
                return
        self.items.append(elem)             


    def __eq__( self, setB ):       	
        if self.size() != setB.size() :	
            return False
        for idx in range(len(self.items)): 			
            if self.items[idx] != setB.items[idx] :	
                return False
        return True

    def union( self, setB ):        	
        newSet = Set()					
        a = 0							
        b = 0							
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]		
            if valueA < valueB :		
                newSet.items.append( valueA )	
                a += 1					
            elif valueA > valueB :		
                newSet.items.append( valueB )	
                b += 1			
            else : 				
                newSet.items.append( valueA )	
                a += 1					
                b += 1
        while a < len( self.items ):	
             newSet.items.append( self.items[a] )
             a += 1
        while b < len( setB.items) :	
             newSet.items.append( setB.items[b] )
             b += 1
        return newSet					

#======================================================================
# 7.5절
#======================================================================
def sequential_search(A, key, low, high) :	
    for i in range(low, high+1) :			
        if A[i].key == key :  				
            return i 						
    return None							    


def binary_search(A, key, low, high) :
	if (low <= high) :				        
		middle = (low + high) // 2	        
		if key == A[middle].key :		    
			return middle
		elif (key<A[middle].key) :	        
			return binary_search(A, key, low, middle - 1)
		else :						
			return binary_search(A, key, middle + 1, high)
	return None        				

def binary_search_iter(A, key, low, high) :
	while (low <= high) :       		
		middle = (low + high) // 2
		if key == A[middle].key:	    
			return middle
		elif (key > A[middle].key):	
			low = middle + 1		
		else:						
			high = middle - 1		
	return None        				


#======================================================================
# 7.7절
#======================================================================
class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

    def __str__( self ):
        return str("%s:%s"%(self.key, self.value) )

class SequentialMap:							
    def __init__( self ):
        self.table = []					    	

    def size( self ): return len(self.table)	
    def display(self, msg):				    	
        print(msg)
        for entry in self.table :				
            print("  ", entry)					

    def insert(self, key, value) :				
        self.table.append(Entry(key, value))	

    def search(self, key) :             		
        pos = sequential_search(self.table, key, 0, self.size()-1)
        if pos is not None : return self.table[pos]
        else : return None

    def delete(self, key) :					
        for i in range(self.size()):
            if self.table[i].key == key :	
                self.table.pop(i)			
                return

map = SequentialMap()						
map.insert('data', '자료')					
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')	
map.display("나의 단어장: ")			

print("탐색:game --> ", map.search('game'))	
print("탐색:over --> ", map.search('over'))
print("탐색:data --> ", map.search('data'))

map.delete('game')						
map.display("나의 단어장: ")

#----------------------------------------------------------------------
class Node:
    def __init__( self, data, link=None ):
        self.data = data
        self.link = link

class HashChainMap:						
    def __init__( self, M ):
        self.table = [None]*M			
        self.M = M

    def hashFn(self, key) :				
        sum = 0
        for c in key :					
            sum = sum +  ord(c)			
        return sum % self.M

    def insert(self, key, value) :		
        idx = self.hashFn(key)			
        self.table[idx] = Node(Entry(key,value), self.table[idx])	

    def search(self, key) :
        idx = self.hashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key :
                return node.data
            node = node.link
        return None

    def delete(self, key) :
        idx = self.hashFn(key)
        node = self.table[idx]
        before = None
        while node is not None:         		
            if node.data.key == key :   		
                if before == None :     		
                    self.table[idx] = node.link
                else :                  		
                    before.link = node.link
                return
            before = node						
            node = node.link					

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)) :
            node = self.table[idx]
            if node is not None :
                print("[%2d] -> "%idx, end='')
                while node is not None:
                    print(node.data, end=' -> ')
                    node = node.link
                print()


#----------------------------------------------------------------------

d = {}									
d['data'] =  '자료'						
d['structure'] = '구조'
d['sequential search'] = '선형 탐색'
d['game'] = '게임'
d['binary search'] = '이진 탐색'
print("나의 단어장:")
print(d)								

if d.get('game') : print("탐색:game --> ", d['game'])
if d.get('over') : print("탐색:over --> ", d['over'])
if d.get('data') : print("탐색:data --> ", d['data'])

d.pop('game')						
print("나의 단어장:")
print(d)