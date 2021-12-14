inputList = []
numIncreases = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(int(line))
prevNum = inputList[0]
for i in inputList:
    if i > prevNum:
        numIncreases += 1
    prevNum = i
print(numIncreases)