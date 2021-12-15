inputList = []
depth = 0
xPos = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line.split())
for i in inputList:
    if i[0] == "forward":
        xPos += int(i[1])
    elif i[0] == "down":
        depth += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])

#print(inputList)
print("depth " + str(depth) + ", xPos " + str(xPos))
print(depth*xPos)