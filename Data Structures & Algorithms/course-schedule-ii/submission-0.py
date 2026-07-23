class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        '''

        prerequisites -> dependencies -> DFS

        
        output = []
        visit = set()

        1. build adjacency list
        
        #the whole point of this dfs is to return True if a course can be completed, and return False if a course cant be completed
        2. define dfs(node) 
            if node in visit: #cycle detected, return False
                return False
            
            #if node has no dependencies, return True
            if not adj[node]:
                return True
            
            visit.add(node)
            
            #search neighbors
            #if all prereq's return True -> we know that all prereq's can be completed -> course can be completed
            for prereq in adj(node):
                #if prereq cant be completed -> course cant be completed -> return False
                if not dfs(prereq):
                    return False
            
            #at this point, all prereq's can be completed -> course can be completed
                #if course can be completed -> wipe adjlist -> return True
            
            visit.remove(node)
            adj(node) = []
            output.append(node)
            return True
        

        3. run dfs on every node

            for node in range(0, numCourses)
                if not dfs(node):
                    return []
            
        4. return output

        '''

        #initialize variables
        output = []
        visit = set()
        adj = [[] for _ in range(0, numCourses)] #initializes an empty list for every node

        #build adj list

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        # dfs

        def dfs(node):
            if node in visit: #if cycle detected, return empty list
                return False
            
            # if node has no prereq's -> course cna be taken -> return True
            if not adj[node]:
                if node not in output:
                    output.append(node)
                return True
            
            # we know we need to search further. add to visit and do dfs recursively

            visit.add(node)

            for prereq in adj[node]:
                if not dfs(prereq):
                    return False
            
            # at this point, course can be taken because all prerequisite courses can be taken
            
            adj[node] = []
            visit.remove(node)
            output.append(node)
            return True
        
        # run dfs on every course to see if every course can be taken
        for node in range(0, numCourses):
            if not dfs(node):
                return []
        
        return output
            






        
        