
def findLongestSubstring(string):
    n = len(string)
    st = 0
    currlen = 0
    maxlen = 0
    start= 0
    pos = {}

    for i in range(0,n):
        if string[i] not in pos:
            pos[string[i]] = i

        else:
            if pos[string[i]] >= st:
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
            st = pos[string[i]] + 1
        pos[string[i]] = i


    if maxlen < i - st:
        maxlen = i - st
        start = st
    return string[start+1:maxlen+1]

print findLongestSubstring('ABDEFGABEF')
