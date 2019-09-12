from collections import deque, defaultdict
def alien_order(words):
    hash_map = defaultdict(list)
    in_map = defaultdict(int)
    hash_set = set(''.join([word for word in words]))
    result = []
    
    for index in range(len(words) - 1):
        first = words[index]
        second = words[index + 1]
        char_length = 0
        length = min(len(first), len(second))
        for index2 in range(length):
            if first[index2] != second[index2]:
                hash_map[first[index2]].append(second[index2])
                break
            char_length += 1
        
        if char_length == length and len(first) > len(second):
            return ""
        
    for chars in hash_map.values():
        for char in chars:
            in_map[char] += 1
    queue = deque()
    for char in hash_set:
        if char not in in_map:
            queue.append(char)
            result.append(char)

    while queue:
        char_out = queue.popleft()
        for char_in in hash_map[char_out]:
            in_map[char_in] -= 1
            if in_map[char_in] == 0:
                queue.append(char_in)
                result.append(char_in)

    return ''.join(result) if len(result) == len(hash_set) else ""


if __name__ == '__main__':
    words = [
              "wrt",
              "wrf",
              "er",
              "ett",
              "rftt"
            ]
    print(alien_order(words))

