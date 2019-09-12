from collections import deque
def remove_invalid_parentheses(string):
    if not string:
        return [""]
    
    def is_valid(new_string):
        count = 0
        for char in new_string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return not count
    
    result = []
    hash_set = set()
    queue = deque([string])
    found = False
    while queue:
        item = queue.popleft()
        if is_valid(item):
            result.append(item)
            found = True
        if found:
            continue
        for index in range(len(item)):
            if item[index] != '(' and item[index] != ')':
                continue
            new_string = item[:index] + item[index + 1:]
            if new_string not in hash_set:
                queue.append(new_string)
                hash_set.add(new_string)
    
    return result


if __name__ == '__main__':
    # s = '()())()'
    s = '(a)())()'
    # s = ')('
    print(remove_invalid_parentheses(s))