inputList = []
depth = 0
xPos = 0
aim = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line.split())
for i in inputList:
    if i[0] == "down":
        aim += int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])
    elif i[0] == "forward":
        xPos += int(i[1])
        depth += int(i[1])*aim

#print(inputList)
print("depth " + str(depth) + ", xPos " + str(xPos))
print(depth*xPos)