def my_len( data ):
    count = 0
    for i in data:
        count += 1
    return count

def my_split(str, ch):
    index = -1
    l = []
    start = 0
    for i in str:
        index += 1
    
        if ch[0] == i:
            if ch == str[index:index + my_len(ch)]:
                l.append(str[start:index])
                start = index + my_len(ch)
    l.append(str[start:])    
    return l

a = 'apple and banana and peach and totmato and lemon and grape and lime'
print(my_split(a, 'and'))

def my_max(a):
    i = 0
    for j in range(my_len(a)):
        if a[i] < a[j]:
            i = j
            result = a[i]
        result = a[i]
    return result

a = range(101)
print(my_max(a))

def my_min(a):
    i = 0
    for j in range(my_len(a)):
        if a[i] > a[j]:
            i = j
            result = a[i]
        result = a[i]
    return result

print(my_min(a))

def my_sum(a):
    count = 0
    for i in a:
        count += i
    return count

print(my_sum(a))

def my_avg(a):
    count = 0
    for i in a:
        count += i
    return count / my_len(a)

print(my_avg(a))
print(my_avg((3,4)))