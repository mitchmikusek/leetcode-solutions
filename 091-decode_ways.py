"""
    12345
    27342
    
    For string X and distance Y into string, ways of decoding increases as we have acceptable branching paths
    branching paths are introduced when the current character and the next could be intrepreted as a single value
    Paths are not acceptable if they would cause an invalid character's occurance ( < 1 or > 20)
"""
# DP + Memoization - Time O(n) / Space O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.num_ways(s)
        
    def num_ways(self, s:str):
        k = len(s)
        memo = [None] * (k + 1)
        return self.num_ways_helper(s, k, memo)
    
    def num_ways_helper(self, s:str, k:int, memo:list):
        i = len(s) - k
    
        if k == 0: return 1
        if s[i] == "0": return 0

        if memo[k] != None:
            return memo[k]
        
        result = self.num_ways_helper(s, k-1, memo)
        if k>1 and int(s[i:i+2]) < 27: # Make sure to check substring position +2, or be left debugging :)
            result = result + self.num_ways_helper(s, k-2, memo)
        
        memo[k] = result
        return result


"""

"0"     -> 0
""      -> 1
"1-9"   -> 1
"10-26" -> String, remaining string for both digits
>26     -> string, remaining for single digit

"12345" - 1: + (2345)  -  k-1
          12: + (345)  - k-1

"27345" - 2: + (7345)
        string, k-1
"""
# Direct - Time O(2^n) / Space O(1)
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         return self.numDecodingHelper(s, n)
    
#     def numDecodingHelper(self, string: str, remaining: int):
#         if remaining == 0: return 1
        
#         i = len(string) - remaining
#         if string[i] == "0": return 0 

#         result = self.numDecodingHelper(string, remaining-1)

#         if remaining >= 2 and int(string[i : i+2]) <= 26:
#             result = result + self.numDecodingHelper(string, remaining-2)
            
#         return result
    
# DP + Memoization - Time O(n) / Space O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [None] * (n + 1)
        return self.numDecodingHelper(s, n, memo)
    
    def numDecodingHelper(self, string: str, remaining: int, memo: list):
        if remaining == 0: return 1
        
        i = len(string) - remaining
        if string[i] == "0": return 0 

        if memo[remaining] != None:
            return memo[remaining]
        
        result = self.numDecodingHelper(string, remaining-1, memo)

        if remaining >= 2 and int(string[i : i+2]) <= 26:
            result = result + self.numDecodingHelper(string, remaining-2, memo)
        
        memo[remaining] = result
        return result
        


