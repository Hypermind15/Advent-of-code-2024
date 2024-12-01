data = open("D:\\Rowan\\Documents\\Coding\\Python\\Advent of code\\2024\\01 data.dat", "r")

list1 = []
list2 = []

for line in data.readlines():
    list1.append(int(line[0:5 ]))
    list2.append(int(line[8:13]))

list1.sort()
list2.sort()

#Part 1
distanceScore = 0

for i in range(len(list1)):
    distanceScore += abs(list1[i] - list2[i])

print(distanceScore)

#Part 2
similarityScore = 0

for i in list1:
    similarityScore += i * list2.count(i)

print(similarityScore)