#Edit distance is also known as Levenshtein Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Get Word Lengths
        n = len(word1)
        m = len(word2)
        
        #Build Dynamic programming Distnace Matrix
        dm = [ [0] * ( m + 1 ) for i in range( n + 1 ) ]
        for i in range(n+1): dm[i][0] = i
        for j in range(m+1): dm[0][j] = j
        
        #Iterate over matrix spaces
        for i in range(1, n+1):
            for j in range(1, m+1):
                #Grab surrounding values
                diag = dm[i-1][j-1]
                left = dm[i][j-1]
                top = dm[i-1][j]
                
                #If our current charaters are equal, current val = diag
                if word1[i-1] == word2[j-1]: 
                    dm[i][j] = diag
                #Otherwise, current val equals the min of the surrounding values + 1
                else:    
                    dm[i][j] = min(diag, left, top) + 1
        #return the distance count for each full string
        return dm[n][m]
    