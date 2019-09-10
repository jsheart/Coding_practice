def wood_cut(woods, k):
    right = max(woods)
    left = 0
    longest = 0
    while left <= right:
        length = left + (right - left) // 2
        count = 0
        for wood in woods:
            count += wood // length
        if count >= k:
            longest = max(longest, length)
            left = length + 1
        else:
            right = length - 1
    return longest

if __name__ == '__main__':
    woods = [232, 124, 456]
    k = 7
    print(wood_cut(woods, k))