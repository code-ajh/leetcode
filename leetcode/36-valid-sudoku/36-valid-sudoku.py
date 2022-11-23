class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        candidate_list  : dict[str, list[tuple]] = dict()
        
        for idx, row in enumerate(board):
            for loc in range(len(row)):
                if row[loc] != ".":
                    
                    if candidate_list.get(row[loc]):
                        candidate_list[row[loc]].append((idx,loc))
                    else:
                        candidate_list[row[loc]] = [(idx, loc)]
                    
        
        for _, values in candidate_list.items():
            
            x = set(x[0] for x in values)
            y = set(y[1] for y in values)
            block = set((x//3,y//3) for x, y in values)
                        
            if len(values) == len(x) and len(values) == len(y) and len(values) == len(block):
                continue
            else:
                return False
            
                
        return True