class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''

        given list of edges -> build adjacency list

        detect cycle -> DFS




        '''

        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)

        visit = set()
        
        def dfs(course):
            
            if course in visit: #cycle detected -> return False
                return False
            
            if not adj[course]:
                return True 

            visit.add(course)

            for prereq in adj[course]:
                if not dfs(prereq): # if a pre req cant be completed -> course cant be completed -> return false
                    return False
                
            adj[course] = []
            visit.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
            