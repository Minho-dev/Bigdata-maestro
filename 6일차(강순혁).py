l=list(range(10))

for i in range(0,10,1):
    l[i]=int(input("no:"))

def my_max(l):
    max=l[0]
    for t in range(10):
        if l[t]>max:
            max=l[t]

    return max

print(my_max(l))

#최솟값

k=list(range(10))

for e in range(0,10,1):
    k[e]=int(input("reno:"))

def my_min(k):
    min=k[0]
    for w in range(10):
        if k[w]<min:
            min=k[w]

    return min

print(my_min(k))

#합

a=(1,2,3,4,5,6,7,8,9,10)

def my_sum(a):
    result=0
    for i in range(len(a)):
        result += a[i]

    return result

print(my_sum(a))

def my_avg(a):
    result=0
    leng=(len(a))
    for i in range(len(a)):
        result += a[i]
    t=result/leng

    return t

print(my_avg(a))
