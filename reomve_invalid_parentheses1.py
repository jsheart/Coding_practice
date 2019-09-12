def remove_invalid_parentheses(string):
    if not string:
        return ""
    count = 0
    index = 0
    while index < len(string):
        if string[index] == '(':
            count += 1
        elif string[index] == ')':
            if count == 0:
                tmp = string[:index] + string[index + 1:]
                if not tmp:
                    return ""
                string = tmp
                index -= 1
            else:
                count -= 1
        index += 1
    
    count = 0
    index = len(string) - 1
    while index > -1:
        if string[index] == ')':
            count += 1
        elif string[index] == '(':
            if count == 0:
                tmp = string[:index] + string[index + 1:]
                if not tmp:
                    return ""
                string = tmp
                index += 1
            else:
                count -= 1
        index -= 1
    
    return string


if __name__ == '__main__':
    # s = '()())()'
    s = '(a)())()'
    # s = ')('
    print(remove_invalid_parentheses(s))