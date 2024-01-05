#======================================================================
# 4.2절
#======================================================================
top = [ ]	                

def isEmpty():
    return len(top) == 0	

def push(item):
    top.append(item)		

def pop():
    if not isEmpty():		
        return top.pop(-1)	

def peek():			       
    if not isEmpty():		
        return top[-1]		

def size(): return len(top)
def clear(): 
	global top		       
	top = []		       


for i in range(1,6):		
    push(i)			       
print(' push 5회: ', top)	
print(' pop() --> ', pop())
print(' pop() --> ', pop())
print(' pop  2회: ', top)	


push('홍길동')
push('이순신')
print(' push+2회: ', top)	
print(' pop() --> ', pop())	
print(' pop  1회: ', top)	

#----------------------------------------------------------------------
class Stack :
    def __init__( self ):   
        self.top = []       

    def isEmpty( self ): return len(self.top) == 0
    def size( self ): return len(self.top)
    def clear( self ): self.top = []	

    def push( self, item ):
        self.top.append(item)

    def pop( self ):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self ):
        return str(self.top[::-1])

odd = Stack()				        
even = Stack()				        
for i in range(10):		    	    
    if i%2 == 0 : even.push(i) 		
    else : odd.push(i)			    
print(' 스택 even push 5회: ', even)
print(' 스택 odd  push 5회: ', odd)	
print(' 스택 even     peek: ', even.peek())
print(' 스택 odd      peek: ', odd.peek())	
for _ in range(2) : even.pop()		
for _ in range(3) : odd.pop()		
print(' 스택 even  pop 2회: ', even)
print(' 스택 odd   pop 3회: ', odd)	


#======================================================================
# 4.3절
#======================================================================	
def checkBrackets(statement):
    stack = Stack()
    for ch in statement:		    
        if ch in ('{', '[', '('):	
            stack.push(ch)
        elif ch in ('}', ']', ')'):	
            if stack.isEmpty() :
                return False		
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False	

    return stack.isEmpty()		    

str = ( "{ A[(i+1)] = 0; }", "if( (i==0) && (j==0 )", "A[ (i+1] ) = 0;" )
for s in str:
    m = checkBrackets(s)
    print(s," ---> ", m)


#======================================================================
# 4.4절
#======================================================================	
def evalPostfix( expr ):
    s = Stack()			       
    for token in expr :			
        if token in "+-*/" :	
            val2 = s.pop()		
            val1 = s.pop()		
            if (token == '+'): s.push(val1 + val2)	
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :				        
            s.push( float(token) )	

    return s.pop()		        	


expr1 = [ '8', '2', '/', '3', '-', '3', '2', '*', '+']
expr2 = [ '1', '2', '/', '4', '*', '1', '4', '/', '*']
print(expr1, ' --> ', evalPostfix(expr1))
print(expr2, ' --> ', evalPostfix(expr2))


#----------------------------------------------------------------------
def precedence (op):			        
    if   op=='(' or op==')' : return 0	
    elif op=='+' or op=='-' : return 1	
    elif op=='*' or op=='/' : return 2	
    else : return -1


def Infix2Postfix( expr ):		
    s = Stack()
    output = []			        
    for term in expr :
        if term in '(' :		
            s.push('(')			
        elif term in ')' :		
            while not s.isEmpty() :
                op = s.pop()
                if op=='(' : break;	
                else :			    
                    output.append(op)
        elif term in "+-*/" :		
            while not s.isEmpty() :	
                op = s.peek()		
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)		
        else :				    
            output.append(term)	

    while not s.isEmpty() :		
        output.append(s.pop())	

    return output	


infix1 = [ '8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = [ '1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)
print('  중위표기: ', infix1)
print('  후위표기: ', postfix1)
print('  계산결과: ', result1, end='\n\n')
print('  중위표기: ', infix2)
print('  후위표기: ', postfix2)
print('  계산결과: ', result2)


#======================================================================
# 4.5절
#======================================================================	
def isValidPos(x, y) :		
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False		
    else :			        
        return map[y][x] == '0' or map[y][x] == 'x'


def DFS() :			   
    stack = Stack()		
    stack.push( (0,1) )
    print('DFS: ')

    while not stack.isEmpty(): 	
        here = stack.pop()	    
        print(here, end='->')
        (x, y) = here		     
        if (map[y][x] == 'x') :	
            return True
        else :
            map[y][x] = '.'	
            
            if isValidPos(x, y - 1): stack.push((x, y - 1)) 
            if isValidPos(x, y + 1): stack.push((x, y + 1)) 
            if isValidPos(x - 1, y): stack.push((x - 1, y)) 
            if isValidPos(x + 1, y): stack.push((x + 1, y)) 
        print(' 현재 스택: ', stack)	
    return False			            


map = [ [ '1', '1', '1', '1', '1', '1' ],
	  [ 'e', '0', '0', '0', '0', '1' ],
	  [ '1', '0', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '0', '0', 'x' ],
	  [ '1', '1', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6
result = DFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')