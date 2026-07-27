class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        '''

        1. create an adjacency list of the graph based on prereq list

        2. do dfs for each node to see if each course can be taken

        




        '''

        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        

        #dfs

        visit = set()

        def dfs(course, adj, visit):
            if course in visit:
                return False #cycle detected
            
            #if no prereq's -> course can finish -> return True

            if adj[course] == []:
                return True
            #add to visit set

            visit.add(course)

            #search prereq's

            for prereq in adj[course]:
                if not dfs(prereq, adj, visit):
                    return False #course cant be finished, return False
                
                #course can be finished since all prereq's can be finished -> wipe adj[course] and return True

            adj[course] = []
            visit.remove(course)
            return True
            
        
        for n in range(numCourses):
            if not dfs(n, adj, visit):
                return False
        
        return True
                



        