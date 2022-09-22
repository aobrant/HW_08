
import copy


class Stack:

    def __init__(self,stack:list) -> None:
        
        self.stack = copy.deepcopy(stack)
    
    def isEmpty(self) -> bool:
 
        if self.stack:
            return False
        else: 
            return True       

    def push(self,element) -> None:

        self.stack.append(element)

    def pop(self):

        s = len(self.stack)
        p = self.stack.pop(s-1)
        return p


    def peek(self):

         s = len(self.stack)
         pk = self.stack[s-1]
         return pk

    def size(self) -> int:

        s = len(self.stack) 
        return s

    def ls(self):

        ls = list(self)
        return





        





    
