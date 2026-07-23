class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        '''


        valid tree -> no cycles, fully connected -> Union-Find

        for n1, n2 in edges:
            if not union(n1,n2) # if union(n1,n2) returns false, nodes were already i nthe same set, and adding will create a cycle -> invalid tree -> return false
                return false
            
            #n1 and n2 merge together 
        
        if we go through all the edges without returning false, it means all the edges successfully merged together and are connected without creating cycles
            


        '''

        par = {}
        rank = {}

        #initialize all parents to themselves, all ranks = 0
        for i in range(0, n):
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
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return False

        
        return len(edges) == n-1



        