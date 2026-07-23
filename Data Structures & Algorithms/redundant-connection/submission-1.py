class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        '''

        output: an edge that can be removed so the graph is still a connected non cyclical graph
            if multiple edges, return edge that appears last in "edges" variable

        
        Union Find -> Detects if a graph has a cycle
                    -> Connects graphs together

        

        1. perform union find on edges one at a time
            initialize
            find
            union
            
        2. stop when all nodes are connected and non cyclical 
        3. return last edge not used


        '''

        par = {}
        rank = {}

        #initialize all parents to themselves, all ranks = 0
        for i in range(1, len(edges)+1):
            par[i] = i
            rank[i] = 0
        
        # function returns the root parent of the node
        def find(node):
            p = par[node]
            #while the node's parent is not itself, search for grandparent
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            #check if nodes are already in same union
            if p1 == p2:
                return False 
            
            # if not, unionize the nodes by having the parent with the higher ranking be the parent of the other node

            if rank[p1] > rank[p2]:
                par[p2] = p1
            else:
                par[p1] = p2
                rank[p2] += 1
            
            return True
        

         #2. stop when all nodes are connected and non cyclical 
        #3. return last edge not used

        removable = []

        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1, n2]



            













        