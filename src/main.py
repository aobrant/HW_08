from stack import Stack

def balance(lst:list) -> None:
    st  = Stack(lst)
    st_new = Stack([])
    size = st.size()
    count = 1
    for i in range(size-1):
        p = st.pop()
        if p == ')' or p == '}' or p == ']':
            st_new.push(p)
        else:   
            st_p = st_new.peek()  
            if st_new.size() != 0 and ((p == '{' and st_p == '}') or (p == '(' and st_p == ')')
                 or (p == '[' and st_p == ']')) :
                 st_new.pop()
            else:
                count = 0
    if count == 0:
        return False
    else:
        return True



   

if __name__ == '__main__':
    
   
    res = balance(list('[([])((([[[]]])))]{()}'))
    if res == True:
        print('Balanced')
    else: 
        print('Not Balanced')
    


