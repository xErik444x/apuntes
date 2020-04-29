a = [8,10,11,1,6,99,723,1231,43,123131,7865,2,643,6]
print(a)
for i in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]

print("Menor a mayor:",a)