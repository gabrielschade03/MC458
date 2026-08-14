binary_tree = input().split()
iterator = 0

def findMaxPath():
    global iterator
    root = int(binary_tree[iterator])
    iterator += 1
    if(binary_tree[iterator] == "T"):
        iterator += 1
        max_left, max_path_left  = findMaxPath()
    else:
        max_left = 0
        max_path_left = 0
        iterator += 1
    
    if(binary_tree[iterator] == "T"):
        iterator += 1
        max_right, max_path_right  = findMaxPath()
    else:
        max_right = 0
        max_path_right = 0
        iterator += 1

    max_path = max(max_path_left + root, max_path_right + root, 0)

    maximum = max(max_left, max_right, max_path_left + max_path_right + root)

    return maximum, max_path

maximum, max_path = findMaxPath()
print(max(maximum, max_path))