a = [16, 19, 11, 15, 10, 12, 14]
print("Unsorted List",a)
for i in a:
    j = a.index(i)
    while j>0:
        if a[j-1] > a[j]:
            a[j-1],a[j] = a[j],a[j-1]
        else:
            break
        j = j-1
print (a)