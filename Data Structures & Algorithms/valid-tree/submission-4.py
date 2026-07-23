class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        '''
        graph is a valid tree if:
        1) has no cycles
        2) is fully connected

        
        1. create adjacency list for undirected graph

        2. dfs
            - since we compare if len(visit) == n at the end, we cant do visit.remove(node)
            - thus, we will track the parent to prevent false cycle detection
                - parent of node 0 = -1
            - if dfs finds a parent node in its neighbors, skip it

            if dfs returns False -> cycle detected -> invalid tree -> return False
        
        3. if len(visit) != n -> disconnected nodes -> invalid tree -> return False


        '''

        visit = set()


        adjList = [[] for i in range(0, n)]

        for n1, n2 in edges:    
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        


        def dfs(node, parent):
            if node in visit:
                return False #cycle detected
            
            visit.add(node)

            for neighbor in adjList[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False
            
            return True
        
        if not dfs(0, -1): 
            return False
        
        return len(visit) == n
        
    










        