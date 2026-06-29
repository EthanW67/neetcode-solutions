class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for crs, preq in prerequisites:
            preMap[crs].append(preq)
        
        result = []

        seen, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True  
            cycle.add(crs)
            for preq in preMap[crs]:
                if dfs(preq) == False:
                    return False
            cycle.remove(crs)
            seen.add(crs)
            result.append(crs) 
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return result



