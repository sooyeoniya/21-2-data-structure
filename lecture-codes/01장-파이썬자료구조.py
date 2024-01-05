#======================================================================
# 1.2절
#======================================================================

def contains(bag, e) :
    return e in bag		

def insert(bag, e) :	
    bag.append(e)		

def remove(bag, e) :	
    bag.remove(e)		

def count(bag):		  
    return len(bag)		


myBag = []			     
insert(myBag, '휴대폰')	
insert(myBag, '지갑')	
insert(myBag, '손수건')	
insert(myBag, '빗')		 
insert(myBag, '자료구조')
insert(myBag, '야구공')	
print('가방속의 물건:', myBag)

insert(myBag, '빗')
remove(myBag, '손수건')
print('가방속의 물건:', myBag)

#======================================================================
# 1.3절
#======================================================================
import time			

myBag = []			
start = time.time()		
insert(myBag, '축구공')	
# ...
end = time.time()		

def insert(bag, e) :
    bag.append(e)	

def insert(bag, e) :
    bag.insert(0, e)

#======================================================================
# 1.3절
#======================================================================
def factorial(n) :			           
    if n == 1 : return 1		       
    else : return n * factorial(n - 1)	

def factorial(n) :	
    result = 1	
    for k in range(n, 0, -1) :
        result = result * k
    return result

#----------------------------------------------------------------------
def power_iter(x, n) : 		 
    result = 1.0
    for i in range(n):		
        result = result * x
    return result

def power(x, n) :
    if n == 0 : return 1
    elif (n % 2) == 0 :			      
        return power(x*x, n//2)		  
    else :
        return x * power(x*x, (n-1)//2)

#----------------------------------------------------------------------
def fib(n) :			   
    if n == 0 : return 0	
    elif n == 1 : return 1	
    else : 
        return fib(n - 1) + fib(n - 2)	

def fib_iter(n) :			
	if (n < 2): return n

	last = 0
	current = 1
	for i in range(2, n+1) :
		tmp = current
		current += last
		last = tmp
	return current

#----------------------------------------------------------------------
def hanoi_tower(n, fr, tmp, to) :		        

    if (n == 1) :				                
        print("원판 1: %s --> %s" % (fr, to))	
    else :
        hanoi_tower(n - 1, fr, to, tmp)		    
        print("원판 %d: %s --> %s" % (n,fr,to))	
        hanoi_tower(n - 1, tmp, fr, to)		    

hanoi_tower(4, 'A', 'B', 'C')			        
