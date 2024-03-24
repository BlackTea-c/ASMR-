import spacy

nlp = spacy.blank("en")

# 导入Doc类
from spacy.tokens import Doc

# 目标文本："spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# 用words和spaces创建一个Doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

'''这个例子中我们用了三个词来创建一个doc。空格存储在一个布尔值的列表中， 
代表着对应位置的词后面是否有空格。每一个词符都有这个信息，包括最后一个词符！
Doc类有三个参数：共享的词汇表，词汇和空格。'''