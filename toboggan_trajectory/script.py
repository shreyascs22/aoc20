f = open("trajectory.txt")
f_lines = [line.strip('\n') for line in f]
j, three_one_count,one_one_count, five_one_count, seven_one_count, one_two_count = 0, 0, 0, 0, 0, 0
for i in range(len(f_lines)):
    if f_lines[i][j%len(f_lines[i])] == '#':
        three_one_count += 1
    j += 3
j = 0
for i in range(len(f_lines)):
    if f_lines[i][j%len(f_lines[i])] == '#':
        one_one_count += 1
    j += 1
j = 0
for i in range(len(f_lines)):
    if f_lines[i][j%len(f_lines[i])] == '#':
        five_one_count += 1
    j += 5
j = 0
for i in range(len(f_lines)):
    if f_lines[i][j%len(f_lines[i])] == '#':
        seven_one_count += 1
    j += 7
j = 0
for i in range(0,len(f_lines),2):
    if f_lines[i][j%len(f_lines[i])] == '#':
        one_two_count += 1
    j += 1
print("Part 1 : ",three_one_count)
print("Part 2 :", three_one_count*one_two_count*one_one_count*five_one_count*seven_one_count)
        