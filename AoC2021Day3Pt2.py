inputList = []
bits = []
oList = []
cList = []
oRate = []
cRate = []

def average(l):
    return sum(l)/len(l)

while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(list(line))

for i in inputList[0]:
    oList.append([])
    cList.append([])
for i in range(len(inputList)):
    for j in range(len(inputList[i])):
        oList[j].append(int(inputList[i][j]))
        cList[j].append(int(inputList[i][j]))
for i in range(len(inputList[0])):
    if average(oList[i]) >= 0.5:
        oKeep = 1
    else:
        oKeep = 0
    keepInstO = []
    for j in range(len(oList[i])):
        if oList[i][j] == oKeep:
            keepInstO.append(j)
    bitsO = oList.copy()
    for j in range(len(bitsO)):
        oList[j] = []
        for k in range(len(bitsO[j])):
            if k in keepInstO:
                oList[j].append(bitsO[j][k])
    if len(oList[0]) == 1:
        for j in oList:
            for k in j:
                oRate.append(str(k))
        break

for i in range(len(inputList[0])):
    if average(cList[i]) >= 0.5:
        cKeep = 0
    else:
        cKeep = 1
    keepInstC = []
    for j in range(len(cList[i])):
        if cList[i][j] == cKeep:
            keepInstC.append(j)
    bitsC = cList.copy()
    for j in range(len(bitsC)):
        cList[j] = []
        for k in range(len(bitsC[j])):
            if k in keepInstC:
                cList[j].append(bitsC[j][k])
    if len(cList[0]) == 1:
        for j in cList:
            for k in j:
                cRate.append(str(k))
        break
    

oRate = int("".join(oRate),2)
cRate = int("".join(cRate),2)
print("oRate " + str(oRate))
print("cRate " + str(cRate))
print("LifeSupport: " + str(oRate*cRate))