class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for i in s:

            if i!=']':
                stack.append(i)
            else:
                temp = ""
                num = ""
                while stack[-1]!="[":
                    temp = stack.pop() + temp
                stack.pop()
                while len(stack)>0 and stack[-1]>="0" and stack[-1]<="9":
                    num = stack.pop() + num
                stack.append(temp*int(num))

        return ''.join(stack)