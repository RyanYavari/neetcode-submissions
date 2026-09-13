class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        '''

        1. create adjacency list

        order = []

        2. run dfs starting on node 1


        '''
        output = []

        adj = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visiting, visited = set(), set()

        def dfs(course):
            if course in visited:
                return True #already classified as a valid course 
            if course in visiting:
                return False #cycle detected
            
            visiting.add(course)

            #search neighbors

            for pre in adj[course]:
                if not dfs(pre):
                    return False
                
            #valid course. add to visited

            visited.add(course)
            visiting.remove(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output
        



            
