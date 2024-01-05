#======================================================================
# 12.2절
#======================================================================

def sortGapInsertion(A, first, last, gap) :
    for i in range(first+gap, last+1, gap) :
        key = A[i]
        j = i - gap
        while j >= first and key<A[j] :	
            A[j + gap] = A[j]			
            j = j - gap
        A[j + gap] = key				

def shell_sort(A) : 					
    n = len(A)
    gap = n//2							
    while gap > 0 :
        if (gap % 2) == 0 : gap += 1	
        for i in range(gap) :
            sortGapInsertion(A, i, n - 1, gap)
        print('     Gap=', gap, A)		
        gap = gap//2					


data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
shell_sort(data)
print("Shell     :", data)

#======================================================================
# 12.3절
#======================================================================
def heapSort1(data):
	heap = MaxHeap()				
	for n in data :             	
	    heap.insert(n)

	for i in range(1,len(data)+1):  
	    data[-i] = heap.delete()	
#----------------------------------------------------------------------
def heapify(arr, n, i): 
    largest = i         
    l = 2 * i + 1       
    r = 2 * i + 2       
  
    if l < n and arr[i] < arr[l]: largest = l 		
    if r < n and arr[largest] < arr[r]: largest = r 
    if largest != i: 								
        arr[i],arr[largest] = arr[largest],arr[i] 	
        heapify(arr, n, largest) 			        

def heapSort(arr): 
    n = len(arr) 
    print("i=", 0, arr)				
    for i in range(n//2, -1, -1): 	
        heapify(arr, n, i) 			
        print("i=", i, arr)			
    print()						    

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 			
        print("i=", i, arr)			


arr = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
heapSort(arr) 
print ("HeapSort: ", arr) 


#======================================================================
# 12.4절
#======================================================================
def merge_sort(A, left, right) :
	if left<right :
		mid = (left + right) // 2		
		merge_sort(A, left, mid)		
		merge_sort(A, mid + 1, right)	
		merge(A, left, mid, right)	    

def merge(A, left, mid, right) :
    global sorted		
    k = left			
    i = left			
    j = mid + 1		    
    while i<=mid and j<=right :
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid :		
        sorted[k:k+right-j+1] = A[j:right+1]	
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]		
    A[left:right+1] = sorted[left:right+1]	    

sorted = []
arr = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
sorted = [0]*len(arr)
merge_sort(arr, 0, len(arr)-1) 
print ("MergeSort: ", arr) 

#======================================================================
# 12.5절
#======================================================================
def quick_sort(A, left, right) :
	if left<right :						
		q = partition(A, left, right)	
		quick_sort(A, left, q - 1)		
		quick_sort(A, q + 1, right)	    

def partition(A, left, right) :
	low = left + 1				        
	high = right					    
	pivot = A[left] 				    
	while (low <= high) :			    
	    while low <= right and A[low] < pivot : low += 1
	    while high >= left and A[high]> pivot : high-= 1

	    if low < high :			
	        A[low], A[high] = A[high], A[low]

	A[left], A[high] = A[high], A[left]	 
	return high					        

arr = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
quick_sort(arr, 0, len(arr)-1) 
print ("quick_sort: ", arr) 

#======================================================================
# 12.6절
#======================================================================
def dp_quick_sort(A, low, high) :
    if low < high : 
        lp, rp = partitionDP(A, low, high)  
        dp_quick_sort(A, low, lp-1)    
        dp_quick_sort(A, lp+1, rp-1)   
        dp_quick_sort(A, rp+1, high)   


def partitionDP(A, low, high) :
    if A[low] > A[high]:               
        A[low], A[high] = A[high], A[low]

    j = low + 1                     
    g = high - 1                    
    k = low + 1                     
    lpVal = A[low]                  
    rpVal = A[high]                 
    while (k <= g) :
        if (A[k] < lpVal) :         
            A[k], A[j] = A[j], A[k] 
            j += 1 

        elif (A[k] >= rpVal) :      
            while (A[g] > rpVal  and  k < g): 
               g -= 1
            A[k], A[g] = A[g], A[k]         
            g -= 1

            if (A[k] < lpVal) :             
                A[k], A[j] = A[j], A[k]     
                j += 1 
        k += 1 

    j -= 1 
    g += 1 
    A[low], A[j] = A[j], A[low]     
    A[high], A[g] = A[g], A[high]   
  
    return j, g     

arr = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
dp_quick_sort(arr, 0, len(arr)-1) 
print ("dp_quick_sort: ", arr) 

#======================================================================
# 12.7절
#======================================================================
from queue import Queue                 
def radix_sort(A) :
    queues = []						    
    for i in range(BUCKETS) :
        queues.append(Queue())			

    n = len(A)
    factor = 1							
    for d in range(DIGITS) :			
        for i in range(n) :				
            queues[(A[i]//factor) % 10].put(A[i])
        i = 0
        for b in range(BUCKETS) :		
            while not queues[b].empty():
                A[i] = queues[b].get()	
                i += 1
        factor *= 10					
        print("step", d+1, A)			

import random
BUCKETS = 10
DIGITS  = 4
data = []
for i in range(10) :
    data.append(random.randint(1,9999))	
radix_sort(data)						
print("Radix: ", data)


#======================================================================
# 12.8절
#======================================================================
MAX_VAL = 1000
def counting_sort(A): 
    output = [0] * MAX_VAL      
    count  = [0] * MAX_VAL      

    for i in A:                 
        count[i] += 1
  
    for i in range(MAX_VAL):    
        count[i] += count[i-1]  
  
    for i in range(len(A)):     
        output[count[A[i]]-1] = A[i] 
        count[A[i]] -= 1

    for i in range(len(A)):     
        A[i] = output[i] 


MAX_VAL = 1000
import random
org = [random.randint(0, MAX_VAL-1) for _ in range(100)]
data = list(org)
print("Data      : ", data)
counting_sort(data)
print("counting_sort : ", data)
#----------------------------------------------------------------------
