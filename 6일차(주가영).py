1. 10개의 정수를 리스트에 저장한 후 가장 큰 값과 가장 작은 값을 출력하는 프로그램'''


l = []

for i in range(10):
    print(i+1, end = " ")
    l.append(int(input("Input Number : ")))


def my_max(list):
    #max_val = sys.float_info.min
    #min_val = sys.float_info.max
    max_val = list[0]
    
    for j in range(10):
        if list[j] > max_val:
            max_val = list[j]
    
    return max_val

def my_min(list):

    min_val = list[0]

    for j in range(10):
        if list[j] < min_val:
            min_val = list[j]

    return min_val

print(my_max(l))
print(my_min(l))
