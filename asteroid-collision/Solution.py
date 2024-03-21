class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for i in asteroids:
            
            if len(stack)==0 or not (stack[-1]>0 and i<0):
                stack.append(i)
            else:
                while len(stack)>0 and stack[-1]>0 and i<0 and abs(i)>abs(stack[-1]):
                    stack.pop()
                if len(stack)==0 or not (stack[-1]>0 and i<0):
                    stack.append(i)
                elif abs(i)==abs(stack[-1]):
                    stack.pop()
        
        return stack
            
