#======================================================================
# 11.2절
#======================================================================
vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    
graph = (vertex, weight)				

def weightSum( vlist, W ):				
    sum = 0								
    for i in range(len(vlist)) :		
        for j in range(i+1, len(vlist)):
            if W[i][j] != None :		
                sum += W[i][j]			
    return sum							

print('AM : weight sum = ', weightSum(vertex, weight))

#----------------------------------------------------------------------
def printAllEdges(vlist, W ):			           
    for i in range(len(vlist)) :
        for j in range(i+1, len(W[i])) :		   
            if W[i][j] != None and W[i][j] != 0 :	
                print("(%s,%s,%d)"%(vlist[i],vlist[j],W[i][j]), end=' ')
    print()

printAllEdges(vertex, weight)

#----------------------------------------------------------------------
graphAL ={'A' : set([('B',29),('F',10)          ]),
        'B' : set([('A',29),('C',16), ('G',15)]),
        'C' : set([('B',16),('D',12)          ]),
        'D' : set([('C',12),('E',22), ('G',18)]),
        'E' : set([('D',22),('F',27), ('G',25)]),
        'F' : set([('A',10),('E',27)          ]),
        'G' : set([('B',15),('D',18), ('E',25)]) }

def weightSum(graph):			
    sum = 0
    for v in graph:             
        for e in graph[v]:      
            sum += e[1]			
    return sum//2				

def printAllEdges(graph):		
    for v in graph:             
        for e in graph[v]:      
            print("(%s,%s,%d)"%(v,e[0],e[1]), end=' ')

print('AL : weight sum = ', weightSum(graphAL))
printAllEdges(graphAL)

#======================================================================
# 11.3절
#======================================================================
parent = []     				
set_size = 0    				

def init_set(nSets) :			
    global set_size, parent 	
    set_size = nSets;			
    for i in range(nSets):		
        parent.append(-1)		

def find(id) :					
    while (parent[id] >= 0) :	
        id = parent[id]			
    return id;					

def union(s1, s2) :				
    global set_size				
    parent[s1] = s2				
    set_size = set_size - 1		

def MSTKruskal(vertex, adj):		
    vsize = len(vertex)             
    init_set(vsize)                 
    eList = []                      

    for i in range(vsize-1) :       
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                eList.append( (i,j,adj[i][j]) )

    eList.sort(key= lambda e : e[2], reverse=True)

    edgeAccepted = 0
    while (edgeAccepted < vsize - 1) :	
        e = eList.pop(-1)       		
        uset = find(e[0])      			
        vset = find(e[1])

        if uset != vset :       		
            print("간선 추가 : (%s, %s, %d)" %
				(vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)   	
            edgeAccepted += 1   	

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)

#----------------------------------------------------------------------

INF = 9999
def getMinVertex(dist, selected) :
    minv = 0	
    mindist = INF
    for v in range(len(dist)) :		
        if not selected[v] and dist[v]<mindist :
            mindist = dist[v]					
            minv = v							
    return minv	

def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize			
    selected = [False] * vsize		
    dist[0] = 0					    

    for i in range(vsize) :			
        u = getMinVertex(dist, selected)
        selected[u] = True			
        print(vertex[u], end=' ')	

        for v in range(vsize) :		
            if (adj[u][v] != None):	
                if selected[v]==False and adj[u][v]< dist[v] :
                    dist[v] = adj[u][v]
    print()

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)


#======================================================================
# 11.4절
#======================================================================
INF = 9999
def choose_vertex(dist, found) :			
    min = INF
    minpos = -1
    for i in range(len(dist)) :				
        if dist[i]<min and found[i]==False:	
            min = dist[i]
            minpos = i
    return minpos;							

def shortest_path_dijkstra(vtx, adj, start) :
    vsize = len(vtx)						
    dist = list(adj[start])					
    path = [start] * vsize					
    found= [False] * vsize					
    found[start] = True						
    dist[start] = 0							

    for i in range(vsize) :
        print("Step%2d: "%(i+1), dist)  	
        u = choose_vertex(dist, found)		
        found[u] = True						

        for w in range(vsize) :				
            if not found[w] :				
                if dist[u] + adj[u][w] < dist[w] :	
                    dist[w] = dist[u] + adj[u][w]	
                    path[w] = u						

    return path							            

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' 	]
weight = [ [0,	    7,		INF,		INF,		3,      10,		INF	],
           [7,		0,	    4,		10,	    2,	    6,	    INF	],
           [INF,	4,		0,		2,		INF,		INF,		INF	],
           [INF,	10,		2,		0,      11,		9,		4   ],
           [3,	    2,	    INF,   	11,		0,      13,		5   ],
           [10,	6,	    INF,		9,      13,		0,		INF	],
           [INF,   INF,		INF,   	4,		5,		INF,		0   ] ]    

print("Shortest Path By Dijkstra Algorithm")
start = 0		
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)) :
    if end != start :
        print("[최단경로: %s->%s] %s" %
				(vertex[start], vertex[end], vertex[end]), end='')
        while (path[end] != start) :
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])
#----------------------------------------------------------------------

INF = 9999
def printA(A):			
    vsize = len(A)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (A[i][j] == INF) : print(" INF ", end='')
            else : print("%4d "%A[i][j], end='')
        print("");

def shortest_path_floyd(vertex, adj) :
    vsize = len(vertex)       	
    A = list(adj)			   	
    for i in range(vsize) :   	
        A[i] = list(adj[i])		

    for k in range(vsize) :		
        for i in range(vsize) :
            for j in range(vsize) :		
                if (A[i][k] + A[k][j] < A[i][j]) :
                    A[i][j] = A[i][k] + A[k][j]
        printA(A)					

print("Shortest Path By Floyd Algorithm")
start = 0		
path = shortest_path_floyd(vertex, weight)

