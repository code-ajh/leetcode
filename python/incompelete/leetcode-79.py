# test case

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"

# board = [["a","a"]]
# word = "aa"

from collections import deque
import copy

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
                    
        char_count = 1
        
        neighbor_nodes = [(1,0), (0,1), (-1,0), (0,-1)]
        
        row_limit :int = len(board)
        loc_limit :int = len(board[0])
        
        start_char :list[tuple] = \
            [(row,loc) \
                for row, x in enumerate(board) \
                for loc, y in enumerate(x) \
                if y == word[0]]
        
        if len(start_char) == 0:
            return False
        elif len(start_char) > 0 and len(word) == 1:
            return True
        
        for node in start_char:
            
            nodes = deque([node])
            temp_board = copy.deepcopy(board)
            temp_board[node[0]][node[1]] = '_'

            while len(nodes) != 0:
                node = nodes.popleft()
                
            
                count_flag :bool = False
                
                for target_node in neighbor_nodes:
                                                    
                    row = target_node[0] + node[0]
                    loc = target_node[1] + node[1]
                                                    
                    if 0 <= row < row_limit and 0 <= loc < loc_limit and temp_board[row][loc] == word[char_count]:
                        if char_count == len(word) -1:
                            return True
                        else:
                            nodes.append((row, loc))
                            temp_board[row][loc] = '_'
                            count_flag = True
                
                if count_flag: 
                    char_count += 1
                else:
                    temp_board[node[0]][node[1]] = board[node[0]][node[1]]
        
        return False
                
            
            
        

if __name__ == "__main__":
    
    solution = Solution()
    
    print(solution.exist(board=board, word=word))