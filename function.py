def input_student_info(students):
    count = 0
    name = input( '학생 이름 입력 ( "end" : quit ) : ' )
    while name != 'end' and count < MAX:
        count = count + 1
        subjects = []
        for x in range( SUBJECT ):
            subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )
            while ( subject < 0 or subject > 100 ):
                print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )

            subjects.append( subject )
        students[name] = [name, subjects]
        name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )
    return



def calc_score_table( students ):
    total = 0
    for i in students:
        for subject in students[i][1]:
            total += subject
        
        average = total / SUBJECT
        if average >= 90:
            grade = 'Excellent'
        elif average <= 60:
            grade = 'Fail'
        else:
            grade = ' '
        students[i].append(total)
        students[i].append(average)
        students[i].append(grade)
    return


def clac_rank(students):
    keys = list( students.keys() )

    for i in range( len( students ) ):
        students[ keys[ i ] ].append( 1 )
        for j in range( len( students ) ):
            if students[ keys[ i ] ][ 3 ] < students[ keys[ j ] ][ 3 ]:
                students[ keys[ i ] ][ 5 ] += 1

    return students


def print_score_table(students):
    keys = list( students.keys() )
    for student_name in keys:
        print( '{0:<10}'.format( students[ student_name ][ 0 ] ), end = '' )
        for subject in students[ student_name ][ 1 ]:
            print( '{0:3}'.format( subject ), end = '' )
        print( '{0:5} {1:6.2f} {3:2} {2:<10}'.format( students[ student_name ][ 2 ], 
                                                      students[ student_name ][ 3 ], 
                                                      students[ student_name ][ 4 ],  
                                                      students[ student_name ][ 5 ] ) )

    return




MAX = 10
SUBJECT = 3

students = {}
input_student_info(students)
calc_score_table( students )
clac_rank( students )
print_score_table(students)
