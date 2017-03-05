D = [['A','B','C','D'],['B','C','E'],['A','B','C','E'],['B','D','E'],['A','B','C','D']]
c=['A','B','C']
a=0
for d in D:
    have=True
    for ci in c:
        if ci not in d:
            have=False
    if have:
        a=a+1
print(a)
