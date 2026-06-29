class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course, preq in prerequisites:
            preMap[course].append(preq)

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)

            for preq in preMap[crs]:
                if not dfs(preq):
                    return False
            
            visit.remove(crs)
            preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True