def func2( wordbook ):
    word_name = input( "수정할 내용을 입력하시오 :" )
    
    WORD_LENGTH = 10
    CLASS_LENGTH = 5
    MEANING_LENGTH = 20

    while word_name != 'end':
        word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, CLASS_LENGTH ) )
    
        word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, MEANING_LENGTH ) )
    
        wordbook[ word_name ] = [ word_name, word_class, word_meaning ]
        word_name = input( "수정할 내용을 입력하시오 :" )
    return wordbook