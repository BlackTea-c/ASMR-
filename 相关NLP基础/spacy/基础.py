import spacy

# 创建一个空白的中文nlp对象;这个也是其核心
nlp = spacy.blank('zh')

doc = nlp('不要停下来啊!')

print(doc.text)



'''当我们在一段文字上调用nlp方法时，spaCy首先会对这段文字分词，然后创建一个文本对象。'''


first_token = doc[0] #token对象
print(first_token)

# enumerate() 是 Python 内置函数，用于将一个可迭代对象（如列表、元组、字符串等）转换为一个枚举对象，同时返回索引和对应的值
for i, token in enumerate(doc):
    print(i, token.text)


#词性
import spacy

# 读取小版本的中文流程
nlp = spacy.load("zh_core_web_sm")

# 处理文本
doc = nlp("丛雨想要吃淀粉肠")

# 遍历词符
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)


#依存关系
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)  #.dep_属性返回预测的依存关系标注。.head属性返回句法头词符。你可以认为这是词在句子中所依附的母词符。



# 处理文本
doc = nlp("微软准备用十亿美金买下这家英国的创业公司,但是我还是喜欢柚子社的作品，80块包邮到家~")

# 遍历识别出的实体 doc.ents
for ent in doc.ents:
    # 打印实体文本及其标注
    print(ent.text, ent.label_)


'''一个小诀窍是可以用spacy.explain这个帮手函数 来快速获得大部分常见的标注和标签定义。
举个例子，可能很多人不知道"GPE"代表的地理政治实体（geopolitical entity）的意思， 
但调用spacy.explain我们就知道这是指国家、城市和州省。
同样这个方法也适用于词性标注和依存关系标注。'''
spacy.explain("GPE")
spacy.explain("NNP")
spacy.explain("dobj")
