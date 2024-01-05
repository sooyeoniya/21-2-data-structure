#======================================================================
# 2.7절
#======================================================================
def find_min_max(A) :		       
    min = A[0]
    max = A[0]
    for i in range(1, len(A)) :		
        if max < A[i] : max = A[i]	
        if min > A[i] : min = A[i]	
    return min, max			       

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
x, y = find_min_max(data)		 
print("(min,max) = ", (x,y))	

#----------------------------------------------------------------------
def sum_range(begin, end, step=1) :	
    sum = 0
    for n in range(begin, end, step) :
        sum += n
    return sum

print("sum = ", sum_range(1, 10))	
print("sum = ", sum_range(1, 10, 2))
print("sum = ", sum_range(step=3, begin=1, end=10))

#======================================================================
# 2.8절
#======================================================================
def calc_perimeter(radius) :
    # global perimeter
    print("파이 값: ", pi)		
    perimeter = 2*pi * radius	

pi = 3.14159			    	
perimeter = 0				    
calc_perimeter(10)
print("원둘레(r=10) = ", perimeter)


#======================================================================
# 2.9절
#======================================================================
# 파일명: my_job.py
import min_max	
import sum		

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("(min,max) = ", min_max.find_min_max(data)) 
print("sum = ", sum.sum_range(1, 10))	   

#----------------------------------------------------------------------
# 파일명: my_job.py
from min_max import *
from sum import *	

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("(min,max) = ", find_min_max(data))
print("sum = ", sum_range(1, 10))		 

#======================================================================
# 2.10절
#======================================================================
class Car :
    def __init__(self, color, speed = 0) :	
        self.color = color		            
        self.speed = speed		            
    def speedUp(self) : self.speed += 10	
    def speedDown(self) : self.speed -= 10	

#======================================================================
# 2.11절
#======================================================================
class Car :
    def __init__(self, color, speed = 0) :	
        self.color = color		            
        self.speed = speed		            
    def speedUp(self) : self.speed += 10	
    def speedDown(self) : self.speed -= 10	

    def isEqual(self, carB) :
        if self.color == carB.color : return True
        else : return False
    def __eq__(self, carB) : return self.color == carB.color

print("car2==car6 : ", car2==car6)
print("car3==car6 : ", car3==car6)

#======================================================================
# 2.12절
#======================================================================
class SuperCar(Car) :
    def __init__(self, color, speed = 0, bTurbo = True) :
        super().__init__(color, speed)	
        self.bTurbo = bTurbo		    

    def setTurbo(self, bTurbo = True) :
        self.bTurbo = bTurbo

    def speedUp(self) :			
        if self.bTurbo : 		
            self.speed += 50	
        else :				    
            super().speedUp()	

    def __str__(self) :
        if self.bTurbo :
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else :
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)

s1.speedUp()
s2.speedUp()
print("슈퍼카1:", s1)
print("슈퍼카2:", s2)