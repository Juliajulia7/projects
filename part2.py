m = "baa"
s = "aabbaaa"


def prefixe(m, s):
    for i in range(len(s)):
        temp=0
        if (i + len(m) <= len(s)):
            for j in range(len(m)):
                if(s[i+j]==m[j]):
                    temp=temp+1
                    if (temp==len(m)):
                        return True
    return False
print(prefixe(m,s))
print('max complexity', len(s)*len(m))

def listle_suffixes(s):
    list=[]
    for i in range (len(s)):
        m=(s[i:len(s)], i)
        list.append(m)
    return list
print(listle_suffixes(s))

def recherche_sequentielle(m,l):
    for i in range (len(l)):
        temp=0
        if(len(m)<=len(l[i][0])):
            for j in range (len(m)):
                if(m[j]==l[i][0][j]):
                    temp=temp+1
                    if (temp == len(m)):
                        return i
    return None

l=listle_suffixes(s)
print(recherche_sequentielle(m,l))

def tri_list(l):
    for i in range(len(l)):
        for j in range (i+1, len(l)):
            if l[i][0] > l[j][0]:
                l[i], l[j] = l[j], l[i]
    return l

ll = print(tri_list(l))

def recherche_dichotomique(l, m):
    lenM=len(m)
    start = 0
    end = len(l) - 1
    while start <= end:
        middle = int((start + end)/ 2)
        midpoint = l[middle][0][0:lenM]
        if midpoint > m:
            end = middle - 1
        elif midpoint < m:
            start = middle + 1
        else:
            return l[middle][1]
    return None


print(recherche_dichotomique(tri_list(l),m))

