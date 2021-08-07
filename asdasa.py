a=[2,3,5,1,10,14]
for i in range(1,(len(a))):
    if a[i]<a[i-1]:
        print("noo")
        break
    else:
        print("hoora")
