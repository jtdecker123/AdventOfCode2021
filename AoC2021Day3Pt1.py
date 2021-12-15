inputList = []
bits = []
gRate = []
eRate = []
def average(l):
    return sum(l)/len(l)

while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(list(line))
for i in inputList[0]:
    bits.append([])
for i in range(len(inputList)):
    for j in range(len(inputList[i])):
        bits[j].append(int(inputList[i][j]))
for i in range(len(inputList[0])):
    if average(bits[i]) > 0.5:
        gRate.append("1")
        eRate.append("0")
    else:
        eRate.append("1")
        gRate.append("0")
gRate = int("".join(gRate),2)
eRate = int("".join(eRate),2)
print("gRate " + str(gRate))
print("eRate " + str(eRate))
print("PowerConsume: " + str(gRate*eRate))