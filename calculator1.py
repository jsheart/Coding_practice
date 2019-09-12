def calculate(string):
    if not string:
        return None
    result = 0
    cur = 0
    sign = 1
    stack = []
    for char in string:
        if char == ' ':
            continue
        elif char.isdigit():
            cur = cur * 10 + int(char)
        elif char == '+':
            result += sign * cur
            cur = 0
            sign = 1
        elif char == '-':
            result += sign * cur
            cur = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * cur
            result *= stack.pop()
            result += stack.pop()
            cur = 0
            
    return result + sign * cur

if __name__ == '__main__':
    string = "(1+(4+5+2)-3)+(6+8)+3"
    print(calculate(string))
    
    
