f = open("binary.txt","r")
f_lines = [line.strip() for line in f]
max_val, id_arr = 0, []
for line in f_lines:
    lower, upper, left, right = 0, 127, 0, 7
    for char in line:
        if char == 'B':
            lower = lower + (upper-lower+1)//2
        elif char == 'F':
            upper = lower + (upper-lower+1)//2 - 1
        elif char == 'R':
            left = left + (right-left+1)//2
        else:
            right = left + (right-left+1)//2 - 1
    if line[6] == 'B':
        row = upper
    else:
        row = lower
    if line[9] == 'L':
        column = left
    else:
        column = right
    score = row*8 + column
    id_arr.append(score)
    if max_val < score:
        max_val = score
print("Part 1 : ", max_val)
id_arr.sort()
for i in range(len(id_arr)-1):
    if id_arr[i+1] - id_arr[i] == 2:
        print("Part 2 : ", id_arr[i] + 1)
        break
    