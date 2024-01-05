#======================================================================
# 10.3절
#======================================================================
mygraph = { "A" : set(["B","C"]),
            "B" : set(["A", "D"]),
            "C" : set(["A", "D", "E"]),
            "D" : set(["B", "C", "F"]),
            "E" : set(["C", "G", "H"]),
            "F" : set(["D"]),
            "G" : set(["E", "H"]),
            "H" : set(["E", "G"])
          }

def dfs(graph, start, visited = set() ):
    if start not in visited :			
        visited.add(start)				
        print(start, end=' ')			
        nbr = graph[start] - visited	
        for v in nbr:					
            dfs(graph, v, visited)		


import collections				        

def bfs(graph, start):
    visited = set([start])              
    queue = collections.deque([start])  
    while queue:                        
        vertex = queue.popleft()        
        print(vertex, end=' ')          
        nbr = graph[vertex] - visited	
        for v in nbr:					
            visited.add(v)              
            queue.append(v)             


#======================================================================
# 10.4절
#======================================================================
def find_connected_component(graph) :
    visited = set()					
    colorList = []					

    for vtx in graph :				
        if vtx not in visited :		
            color = dfs_cc(graph, [], vtx, visited)	
            colorList.append( color )	

    print("그래프 연결성분 개수 = %d " % len(colorList))
    print(colorList)				        

def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited :				
        visited.add(vertex)					
        color.append(vertex)				
        nbr = graph[vertex] - visited		
        for v in nbr:						
            dfs_cc(graph, color, v, visited)
    return color							


#======================================================================
# 10.5절
#======================================================================
def bfsST(graph, start):
    visited = set([start])              
    queue = collections.deque([start])  
    while queue:                        
        v = queue.popleft()             
        nbr = graph[v] - visited        
        for u in nbr:                   
            print("(", v, ",", u, ") ", end="") 
            visited.add(u)              
            queue.append(u)             

bfsST(mygraph, "A")
print()

#======================================================================
# 10.6절
#======================================================================
def topological_sort_AM(vertex, graph) :
    n = len(vertex)
    inDeg = [0] * n             

    for i in range(n) :
        for j in range(n) :
            if graph[i][j] > 0 :
                inDeg[j] += 1   

    vlist = []                  
    for i in range(n) :
        if inDeg[i]==0 : 
            vlist.append(i)

    while len(vlist) > 0 :      
        v = vlist.pop()         
        print(vertex[v], end=' ')  

        for u in range(n) :
            if v != u and graph[v][u] > 0 :
                inDeg[u] -= 1       
                if inDeg[u] == 0 :  
                    vlist.append(u)

vertex = ['A', 'B', 'C', 'D', 'E', 'F' ]
graphAM = [ [ 0,   0,   1,   1,   0,   0 ],
            [ 0,   0,   0,   1,   1,   0 ],
            [ 0,   0,   0,   1,   0,   1 ],
            [ 0,   0,   0,   0,   0,   1 ],
            [ 0,   0,   0,   0,   0,   1 ],
            [ 0,   0,   0,   0,   0,   0 ] ]
print('topological_sort: ')
topological_sort_AM(vertex, graphAM)
print()
#----------------------------------------------------------------------
