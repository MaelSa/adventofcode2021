data = open("day1_data","r")
L = [int(i) for i in data.read().split('\n')]
count = 0
print(L)
for i in range(1,1998):
    previous = L[i-1] + L[i] + L[i+1]
    current = L[i] + L[i+1] + L[i+2]
    if current > previous: 
        count += 1
print(count)