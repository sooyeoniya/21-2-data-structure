#======================================================================
# 3.3절
#======================================================================
items = []			       

def insert(pos, elem) :		
   items.insert(pos, elem)	

def delete(pos) :		   
   items.pop(pos)		   

def getEntry(pos): return items[pos]	

def isEmpty( ):
    if len(items) == 0 :
        return True		
    else :				
        return False	

#def isEmpty( ): return len(items) == 0	

def size( ):	    return len(items)	
def clear( ):      items = []		       

def find(item) : return items.index(item)	
def replace(pos, elem): items[pos] = elem	
def sort() : items.sort()			
def merge(lst) : items.extend(lst)	

def display(msg='ArrayList:' ):		
    print(msg, size(), items)		


display('파이썬 리스트로 구현한 리스트 테스트')
insert(0, 10);		insert(0, 20);    insert(1, 30)
insert(size(), 40);	insert(2, 50)
display("파이썬 리스트로 구현한 List(삽입x5): ")
sort()
display("파이썬 리스트로 구현한 List(정렬후): ")
replace(2, 90)
display("파이썬 리스트로 구현한 List(교체x1): ")
delete(2);	delete(size() - 1);	delete(0)
display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [ 1, 2, 3 ]
merge(lst)
display("파이썬 리스트로 구현한 List(병합+3): ")
clear()
display("파이썬 리스트로 구현한 List(정리후): ")


#----------------------------------------------------------------------
class ArrayList:		  
    def __init__( self ):
        self.items = []		

    def insert(self, pos, elem) :
        self.items.insert(pos, elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty( self ):
        return self.size() == 0
    def getEntry(self, pos) :
        return self.items[pos]
    def size( self ):
        return len(self.items)
    def clear( self ) :
        self.items = []	
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem
    def sort(self) :
        self.items.sort()
    def merge(self, lst) :
        self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, self.size(), self.items)

s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10);		s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);		s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")
s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [ 1, 2, 3 ]
s.merge(lst)
s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear()
s.display("파이썬 리스트로 구현한 List(정리후): ")

#======================================================================
# 3.4절
#======================================================================
def myLineEditor() :	
    list = ArrayList()	
    while True :
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")
        if command == 'i' :		
            pos = int( input("  입력행 번호: "))
            str = input("  입력행 내용: ")	    
            list.insert(pos, str)		
        elif command == 'd' :			
            pos = int( input("  삭제행 번호: "))
            list.delete(pos)			
        elif command == 'r' :			
            pos = int( input("  변경행 번호: "))
            str = input("  변경행 내용: ")	    
            list.replace(pos, str)		        
        elif command == 'q' : return	        
        elif command == 'p' :		            
            print('Line Editor')
            for line in range (list.size()) :   
                print('[%2d] '%line, end='')    
                print(list.getEntry(line))      
            print()			                    
        elif command == 'l' :			        
            filename = 'test.txt'
            infile = open(filename , "r")       
            lines = infile.readlines()	        
            for line in lines:		            
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()			
        elif command == 's' :		
            filename = 'test.txt'
            outfile = open(filename , "w")
            for i in range(list.size()) :
                outfile.write(list.getItem(i)+'\n')
            outfile.close()

myLineEditor()


#======================================================================
# 3.5절
#======================================================================
class Set:				        
    def __init__( self ):		
        self.items = []			

    def size( self ): 			
        return len(self.items)	
    def display(self, msg):		
        print(msg, self.items)	

#    def contains(self, item) :
#       return item in self.items

    def contains(self, item) :
        for i in range(len(self.items)):
            if self.items[i] == item :	
                return True
        return False		

    def insert(self, elem) :
        if elem not in self.items :
           self.items.append(elem)

    def delete(self, elem) :
        if elem in self.items :
           self.items.remove(elem)

    def union( self, setB ):		    
        setC = Set()			        
        setC.items = list(self.items)	
        for elem in setB.items :	    
            if elem not in self.items :	
                setC.items.append(elem)	
        return setC			            

    def intersect( self, setB ):	
        setC = Set()
        for elem in setB.items :	
            if elem in self.items :	
                setC.items.append(elem)	
        return setC

    def difference( self, setB ):	    
        setC = Set()
        for elem in self.items:		    
            if elem not in setB.items:	
                setC.items.append(elem)	
        return setC

setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A – B:')