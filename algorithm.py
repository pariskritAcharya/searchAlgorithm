
arr=[3015+x**2 for x in range(100) ]





temp=  arr
temp.sort()
print(temp)

flag=False

#input 
search=int(input())

while len(temp)!=1:
    print(temp)
    print(int(len(temp)/2))
    i =int(len(temp)/2)
    if temp[i]==search:
        flag=True
        break
    if search<temp[i]:
        temp=temp[:i:]
    else:
        temp= temp[i::]

if flag:
    print("found")
else:
    print("not found")