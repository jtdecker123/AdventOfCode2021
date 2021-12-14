inputList = []
numIncreases = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(int(line))
prevSum = inputList[0]+inputList[1]+inputList[2]
i = 2
while i < len(inputList):
    if inputList[i]+inputList[i-1]+inputList[i-2] > prevSum:
        numIncreases += 1
    prevSum = inputList[i]+inputList[i-1]+inputList[i-2]
    i += 1
print(numIncreases)