# test case

maze :list[list[int]] = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrace :list[int] = [1,2]

# maze :list[list[int]] = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
# entrace :list[int] = [3,2]

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        
        now :list[int] = entrance
        candidate_list :list[list[int]] = [now]
        passed_node_list :list[list[int]] = []
        
        x_limit :int = len(maze)
        y_limit :int = len(maze[0])
        
        exit_flag :bool = False
        
        answer :int = 0
            
        
        while True:
            
            temp_list :list[list[int]] = []
                
            for candidate in candidate_list:
                                
                x :int = candidate[0]
                y :int = candidate[1]
                
                candidate[x][y] = '+'
                
                for constant in [-1, 1]:
                    
                    x_copy = x 
                    
                    x_copy += constant
                    
                    if x_copy == -1 or x_copy >= x_limit:
                        if candidate != now:
                            return answer
                        else:
                            continue
                    else:
                        if maze[x_copy][y] == '.':
                            temp_list.append([x_copy, y])
                        else:
                            
                        
                        
                for constant in [-1, 1]:
                    
                    y_copy = y
                    
                    y_copy += constant
                    
                    if y_copy == -1 or y_copy >= y_limit:
                        if candidate != now:
                            return answer
                        else:
                            continue
                    else:
                        if maze[x][y_copy] == '.' and [x,y_copy] not in passed_node_list:
                            temp_list.append([x, y_copy])
                            
            
            
            if exit_flag:
                return answer
            elif len(temp_list) == 0:
                return -1
            else:
                
                candidate_list = temp_list
                answer += 1
                
        return answer
                
                    
                
            


if __name__ == '__main__':
    
    Test = Solution()
    
    answer = Test.nearestExit(maze=maze, entrance=entrace)
    
    print(answer)
    
    
