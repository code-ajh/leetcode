# test case
rooms = [[10,35,25,33],[],[47,27],[23,3,28,39],[36,41,10,24],[14,40,42,44],[41,35],[48],[24,26,44,23,11,17],[1,17,20,30],[],[38,39,44],[],[11,21,45,13],[1,27,14,19],[23],[30,21,8,22,40],[14,48],[32,6],[5,15,26,34,38],[43,25],[18,10,33],[15,34,9],[18,46,48,7,13],[5,29,4],[42,34],[7,13,37,8,15,21],[4,5],[38,20,42],[16,19,47],[8,29],[28,33,37,49],[9,39,49,41],[31,12,26,32],[2,40,32,46],[27,22],[12,37,2],[31,1],[46,19,16,18,30],[35],[6,3,7,28,43],[4,25,2,29],[],[22,24,45,12],[36,31],[3,36,45],[20,43,49],[11],[16,6],[17,47]]

# rooms = [[2,3],[],[2],[1,3]]

class Solution:
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room
        

        

# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.canVisitAllRooms(rooms))