class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {}

        # build graph via adjacency list by using the list of edges
        for src, dst in prerequisites:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)
        

        # now that we have our graph connected, we will run dfs


        visit = set()

        def dfs(node):
            # base case: if node in visit -> cycle detected -> return false
            if node in visit:
                return False

            # base case: if node's pre req's are empty -> return True

            if not adjList[node]: 
                return True
            
            # if not visited and not empty, add to visit and dfs on prereq's

            visit.add(node)
            
            for prereq in adjList[node]:
                # if current course's prereq returns False -> we found one course that cant be completed -> return False
                if not dfs(prereq):
                    return False
            
            # if false isn't returned, then all the prereq's of the course can be completed. Thus:
                #1. remove from visit
                #2. remove all prereqs
                #3. return True

            visit.remove(node)
            adjList[node] = []
            return True
        
        # if every item in the adj list is empty, return True. else false

        for course in adjList:
            if not dfs(course):
                return False
        
        return True

                
                








        