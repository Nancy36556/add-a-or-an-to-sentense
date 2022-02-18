
import nltk
nltk.download('punkt')
sentance = "I love cat "
is_noun= lambda pos:pos [:2] =='NN'
tokenize=nltk.word_tokenize(sentance)
nounx=[word for (word,pos) in nltk.pos_tag(tokenize) if is_noun(pos)]
for i in range(len(nounx)):
    noun= nounx[i]
    if noun[0]=='a' or noun[0]=='i' or noun[0]=='o' or noun[0]=='u':
       sentance=sentance.replace(noun[0],'an'+noun[0])
    else:
        sentance=sentance.replace(noun[0],'a'+noun[0])
print(sentance)

