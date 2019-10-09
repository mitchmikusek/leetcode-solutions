"Travel over empty spaces"
"count pawns"
"blocked by Bishops"

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        directions = ["north", "south", "east", "west"]
        rookLocation = self.findRook(board)
        
        collisions = []
        for direction in directions:
            collisions.append(self.firstCollision(board, rookLocation, direction))
            
        return collisions.count('p')
        
    def findRook(self, board: List[List[str]]):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "R": return [i, j]
    
    def firstCollision(self, board: List[List[str]], position:List[int], direction:str ):
        y = position[0]
        x = position[1]
        
        if direction == "north":    
            while y > 0:
                y = y - 1
                if board[y][x] != ".": return board[y][x]
        elif direction == "south":
            while y < len(board)-1:
                y = y + 1
                if board[y][x] != ".": return board[y][x]     
        elif direction == "west":
             while x > 0:
                x = x - 1
                if board[y][x] != ".": return board[y][x]
        elif direction == "east":
             while x < len(board[y])-1:
                x = x + 1
                if board[y][x] != ".": return board[y][x]        
        return None