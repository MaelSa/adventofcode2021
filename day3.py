data = open("day3_data","r")
L = [i for i in data.read().split('\n')]
count = [0 for i in range(len(L[0]))]
for line in L:
    for c in range(len(line)):
        if line[c]=="1":
            count[c] += 1
a = len(L)//2
gamma = ""
epsilon = ""
for c in count:
    if c > a-1:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'


def getGamma(L):
    n = len(L)
    r = len(L[0])
    count = [0 for i in range(r)]
    for line in L:
        for c in range(r):
            if line[c] == '1':
                count[c] += 1
    
    res = ""
    a = n/2 
    print(count)
    for c in count:
        if c>=a:
            res += "1"
        else:
            res += '0'
    return res

def opp(b):
    res = ''
    for c in b:
        if c == '1':
            res += '0'
        else:
            res += '1'
    return res

listOx = L.copy()
listCo2 = L.copy() 
gamma = getGamma(L)
ox = 0
co2 = 0

for c in range(len(gamma)):
    if len(listOx)!=0:
        gamma = getGamma(listOx)
    if len(listCo2)!=0:
        o = opp(getGamma(listCo2))
    for line in L:
        if line[c] != gamma[c] and line in listOx:
            listOx.remove(line) 
        if line[c] != o[c] and line in listCo2:
            listCo2.remove(line)
    if len(listOx) == 1:
        print(listOx)
        ox = int(listOx[0],2)
    if len(listCo2) == 1:
        print(listCo2)
        co2 = int(listCo2[0],2)
print(ox,co2, ox*co2)