f = open("repair.txt","r")
lines = f.readlines()
fileinput = [int(line.strip()) for line in lines]
res, nres = 0, 0
for i in range(len(fileinput)):
    if (2020 - fileinput[i]) in fileinput:
        val = fileinput.index(2020 - fileinput[i])
        print("Part 1 : ",fileinput[val] * fileinput[i])
        break
for i in range(len(fileinput)):
    for j in range(i+1, len(fileinput)):
        if (2020 - fileinput[i] - fileinput[j]) in fileinput:
            val = fileinput.index(2020 - fileinput[i] - fileinput[j])
            print("Part 2 : ",fileinput[val] * fileinput[i] * fileinput[j])
            break
