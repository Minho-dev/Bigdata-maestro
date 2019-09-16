WORD_LENGTH = 10
CLASS_LENGTH = 5
MEANING_LENGTH = 20

wordbook = {}
count = 0


def result() :
    word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
            
    while word_name != 'end':
        word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, CLASS_LENGTH ) )
        word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, MEANING_LENGTH ) )
        

        word = [ word_name, word_class, word_meaning ]

        wordbook[ word_name ] = word    
        
        word_name = input( '\n최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
    return wordbook

