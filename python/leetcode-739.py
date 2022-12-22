# test case

temperatures = [73,74,75,71,69,72,76,73]


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        # init
        result = [0] * len(temperatures)
        stack = []

        # loop
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)

        return result
            
            

if __name__ == "__main__":
    
    a = Solution()
    
    print(a.dailyTemperatures(temperatures))