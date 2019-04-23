a = [1, 1, 3, 3, 2, 2, 1, 1, 1]
sum =0
dict = {}

for i in a:
    sum = sum + i
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
max = 0
prod = 0
for i in dict.keys():
     prod = i * dict[i]
     diff = sum - prod
     if diff > max:
          max = diff

print max
