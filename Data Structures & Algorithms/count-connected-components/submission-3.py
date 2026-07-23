class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        '''

        counting connected components -> Union-Find

        union-find -> union(n1, n2) function

        connected component = a group of nodes where every node can reach every other node in the group


        union(n1,n2) = False -> two nodes were in same set 
        union(n1,n2) = True -> nodes are in two different sets

        
        strat:
        define union-find algorithm

        res = n # n = num of nodes

        for n1, n2 in edges:
            if union(n1,n2): #if these two nodes are in different sets (different connected components)
                res -= 1
        
        return res



        '''


        par = {}
        rank = {}

        for i in range(0, n):
            par[i] = i
            rank[i] = 0
        

        def find(n):

            p = par[n]

            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2: #already in same set, return false
                return False
            
            if par[p1] > par[p2]:
                par[p2] = p1
            else:
                par[p1] = p2
                rank[p2] += 1
            
            return True



        '''
        the number of connected components = num of nodes - num of unions
        example: if 5 nodes make 5 successful unions -> 0 connected components
                if 5 nodes make 0 successful unions -> 1 connected component 


        '''
        res = n

        for n1, n2 in edges:
            if union(n1,n2): # these two nodes are in different components
                res -= 1
        
        return res


     

    

                











        