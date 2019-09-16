dic = {}
word = input( ' 단어를 입력하세요 ( "end" : quit ) : ' )
while len(dic) <= 50 and word != 'end':
    Class = input( ' 품사를 입력하세요 : ' )
    meaning = input( ' 뜻을 입력하세요 : ' )
    dic[word] = (Class, meaning)
    word = input( ' 단어를 입력하세요 ( "end" : quit ) : ' )
search = input('검색어를 입력하세요 ( "end" : quit ) : ')
while search != 'end':
    if search in dic:
            print( '단어 : {0:<10} 품사 : {1:<10} 뜻 : {2:<10}'.format(search, dic[search][0], dic[search][1]) )
    search = input('\n검색어를 입력하세요 ( "end" : quit ) : ')
print()
