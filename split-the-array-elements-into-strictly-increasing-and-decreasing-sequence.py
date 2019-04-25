# This contains
# a = [7, 2, 2, 2, 2, 3, 1, 4] #TestCase -1 : This is a case where it has more than two occurrences of same element in this case it should fail
# a = [7, 2, 3, 1, 4]# TestCase -2 : This is one test case where all elements are distinct so one array should be empty
a = [7, 2, 3, 7, 3, 1, 4]

a1 = []
a2 = []
dict = {}

for i in a:
    if i in dict and dict[i] < 2:
        dict[i] += 1
        a1.append(i)
    elif i in dict and dict[i] >= 2:
        print "Since %d has occured more than twice it not possible to decide it should be ascending or descending" % (
            i)
        break
    else:
        dict[i] = 1
        a2.append(i)

print sorted(a1)
print sorted(a2, reverse=True)
