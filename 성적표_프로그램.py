'''
    10명의 학생 이름, 점수를 입력 받아, 10명의 학생 이름, 점수을 출력하고
    최고점 학생 정보, 최저점 학생 정보, 평균 점수, 점수대 인원수를 출력하는
    프로그램( 함수로 구현 ) 4시 50분까지 작성 e-mail 제출
'''
'''
필요 data : 학생 한명의 이름, 점수 저장 공간 - student : List
            학생 전체의 이름, 점수 저장 공간 - students : 중첩List
algorithm : 학생 한 명의 이름과 점수를 입력 받는다.
            입력 받은 학생의 정보를 students 리스트에 담는다.
            students 리스트에서 최고점 학생과 최저점 학생을 찾는다.
            평균 점수를 구한다.
            점수대 별 인원수를 구한다.
            구한 정보를 출력한다.
함수 :  inputdata() - 10명 학생 성적 입력 함수
        rank() - 최고점, 최저점 학생 계산 함수
        grade() - 점수대별 구분 함수
        calcaverage() - 평균을 계산하는 함수
        printdata() - 평균 이하의 학생을 출력하는 함수
'''
def inputdata(a):
    student = []
    students = []
    for i in range(a):
        name = input( '이름을 입력하세요 : ' )
        score = int(input( '점수를 입력하세요 : ' ) )
        
        student.append(name)
        student.append(score)
        
        students.append(student)
        
        student = []
    return students

def rank(students):
    max = students[0]
    min = students[0]
    max_min = []
    for i in students:
        if max[1] < i[1]:
            max = i
        if min[1] > i[1]:
            min = i
    
    max_min.append(max)
    max_min.append(min)
    
    return max_min

def calcaverage(students):
    total = 0
    for i in students:
        total += i[1]
    average = total / len(students)

    return average




def grade(students, score):
    count = 0
    for i in students:
        if i[1] >= score and i[1] < score + 10:
            count += 1
    return count



def printdata(students):
    rank1 = rank(students)
    average = calcaverage(students)
    range = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
    print( '{0:>10}'.format( '학생 정보 list' ) )
    for i in students:
        print('{0} {1:<10}'.format(i[0], i[1]))
    
    print()

    print( '최고점 학생 : {0:>5} {1:<5}'.format(rank1[0][0], rank1[0][1]))
    print( '최저점 학생 : {0:>5} {1:<5}'.format(rank1[1][0], rank1[1][1]))
    
    print()

    print( '평균점수 : {0:>5} 점'.format(average))

    print()

    print('점수대별 인원수')
    for i in range:
        count = grade(students, i)
        print('{0:3d}점대 : {1:<5} 명'.format(i, count))
    


student = inputdata(5)
printdata(student)
