class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        '''

        valid tree:
        1. no cycles
        2. all nodes are connected


        '''


        par = {}
        rank = {}

        for i in range(n):
            par[i] = i
            rank[i] = 0
        

        def find(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
            else:
                par[p1] = p2
                rank[p2] += 1
            
            return True
        
        
        # check for cycle by unionizing every edge. if all edges can union properly, then no cycle detected

        for n1, n2 in edges:
            if not union(n1,n2):
                return False
        
        #now that we know theres no cycles, we just need to detect if it's connected as 1 connected compoonent.
        # if len(edges) == n - 1 then every node is connected 

        return len(edges) == n-1

        