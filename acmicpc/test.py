
def Input(string):
    Stack = []
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            Stack.append(string[i])
        elif string[i] == ')':
            if Stack:
                if Stack[-1] == '(':
                    Stack.pop()
                else:
                    print('no')
                    return
            else:
                print('no')
                return
        elif string[i] == ']':
            if Stack:
                if Stack[-1] == '[':
                    Stack.pop()
                else:
                    print('no')
                    return
            else:
                print('no')
                return
    
    if Stack:
        print('no')
        return
    else:
        print('yes')
        return

def _4949():
    while 1:
        string = str(input())
        if string =='.':
            break
        Input(string)


_4949()
