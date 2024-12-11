f = open("pwd.txt")
lines = f.readlines()
start, end, char, string = [], [], [], []
valid, nvalid = 0, 0
for line in lines:
    line = line.strip()
    range_part, char_part, string_part = line.split(' ')
    s, e = range_part.split('-')
    c = char_part[0] 
    start.append(int(s)) 
    end.append(int(e)) 
    char.append(c)            
    string.append(string_part)

for i in range(len(string)):
    if start[i] <= string[i].count(char[i]) <= end[i]:
        valid += 1
print("Part 1 : ",valid)

for i in range(len(string)):
    if (string[i][start[i]-1] == char[i] and string[i][end[i]-1] != char[i]) or (string[i][start[i]-1] != char[i] and string[i][end[i]-1] == char[i]):
        nvalid += 1
print("Part 2 : ",nvalid)