import spacy

nlp = spacy.blank("en")

# 导入Doc类
from spacy.tokens import Doc

# 目标文本："spaCy is cool!"
words = ["spaCy", "is", "cool", "!","but",'...']
spaces = [True, True, False, True,False,False] #表示对应词后面是否加空格

# 用words和spaces创建一个Doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

'''这个例子中我们用了三个词来创建一个doc。空格存储在一个布尔值的列表中， 
代表着对应位置的词后面是否有空格。每一个词符都有这个信息，包括最后一个词符！
Doc类有三个参数：共享的词汇表，词汇和空格。'''



'''一个Span是doc的一段包含了一个或更多的词符的截取。 Span类有最少三个参数：对应的doc以及span本身起始和终止的索引。 
注意终止索引代表的词符是不包含在这个span里面的！'''

# 导入Doc和Span类
from spacy.tokens import Doc, Span

# 创建doc所需要的词汇和空格
words = ["Hello", "world", "!"]
spaces = [True, False, False]
# 手动创建一个doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)
# 手动创建一个span
span = Span(doc, 0, 2)
# 创建一个带标签的span
span_with_label = Span(doc, 0, 2, label="GREETING")
# 把span加入到doc.ents中
doc.ents = [span_with_label]




#从头开始:
import spacy
nlp = spacy.blank('zh')
from spacy.tokens import Doc

words = ["sb","233"]
spaces = [True,False]

doc = Doc(nlp.vocab,words=words,spaces=spaces)

print(doc.text)




