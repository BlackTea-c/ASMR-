'''编写一个定制化组件，使用PhraseMatcher在文本中寻找动物名字，
然后把匹配到的名字加入到doc.ents中。我们已经在变量matcher中创建了含有匹配 动物名模板的PhraseMatcher。
定义这个定制化组件，在doc上面应用matcher。
给每一个匹配结果创建一个Span，添加"ANIMAL"的标签ID，然后 用这些新的span覆盖doc.ents。
处理文本，打印doc.ents中所有实体的实体文本和实体标签。'''


import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("zh_core_web_sm")
animals = ["金毛犬", "猫", "乌龟", "老鼠"] #创建标签集

animal_patterns = list(nlp.pipe(animals)) #传入nlp,形成patterns
print("animal_patterns:", animal_patterns)

#变量matcher中创建了含有匹配 动物名模板的PhraseMatcher
matcher = PhraseMatcher(nlp.vocab) # "匹配器"
matcher.add("ANIMAL", animal_patterns)


@Language.component("animal_component")
def animal_component_function(doc):
    #把matcher应用到doc上
    matches = matcher(doc)
    print('matches:',matches)
    #为每一个匹配结果生成一个span并赋予标签“ANIMAL”
    spans=[Span(doc,start,end,label="ANIMAL") for match_id,start,end in matches]
    print('spans:',spans)
    doc.ents = spans #匹配到的span覆盖实体ent
    return doc

# 把组件加入到流程中，紧跟在"ner"组件后面
nlp.add_pipe("animal_component", after="ner")
print(nlp.pipe_names)

# 处理文本，打印doc.ents的文本和标签
doc = nlp("我养了一只猫和一条金毛犬。")
print([(ent.text, ent.label_) for ent in doc.ents])



doc = nlp.make_doc("Hello world!") #只是用分词器；大多情况下可能我们只需要这个