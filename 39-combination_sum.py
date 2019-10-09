# Also known as the coin changing problem
# Worst case is 2^n 

# [2,3,6,7]
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, canidates, target, index, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(canidates)):
            self.dfs(canidates, target-canidates[i], i, path+[canidates[i]], result )