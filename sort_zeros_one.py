a = [0,1,0,1,0,1,0,1,0,1]
j = len(a)-1
i =0
while (i<=j):
    if a[i] == 0:
        i=i+1
    elif a[j] ==1:
        j = j-1
    elif a[i] == 1 and a[j] == 0 :
        a[i] = 0
        a[j] = 1
        j = j-1
        i = i+1
print a
