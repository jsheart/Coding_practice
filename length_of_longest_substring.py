def length_of_longest_substring(string):
    if len(string) <= 1:
        return len(string)
    max_length = start = 0
    hash_table = {}
    for index, char in enumerate(string):
        if char in hash_table:
            new_start = hash_table[char] + 1
            if new_start > start:
                start = new_start
        max_length = max(max_length, index - start + 1)
        hash_table[char] = index
    return max_length

if __name__ == '__main__':
    string = 'abcabcbb'
    print(length_of_longest_substring(string))