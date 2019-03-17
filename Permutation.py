# def permutation_of_numbers(list_):
#     print list_
#     if len(list_) == 0:
#         return []
#
#     if len(list_) == 1:
#         return [list_]
#     l = []
#
#     for i in range(len(list_)):
#         m = list_[i]
#         remList = list_[:i] + list_[i + 1:]
#
#         for p in permutation_of_numbers(remList):
#             l.append([m] + p)
#     return l
# data1 = '2314'
# data = list('2314')
# m = []
#
# for p in permutation_of_numbers(data):
#     k = ''
#    # print p
#     for j in p:
#         k = k + str(j)
#     m.append(k)
# #print m
# m.sort()
# #print m
#
# for i in range(0,len(m)):
#     if m[i] == data1:
#         pass
#         #print m
#         #print m[i-1]
#
#


def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]
        print '[li]' + str(lst[:i])
        print '[ls]' + str(lst[i+1:])
        print 'rem' + str(remLst)

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    #print p
    pass
