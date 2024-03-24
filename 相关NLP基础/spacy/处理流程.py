




import spacy

# 读取zh_core_web_sm流程
nlp = spacy.load("zh_core_web_sm")

# 打印流程组件的名字
print(nlp.pipe_names)

# 打印完整流程的(name, component)元组
print(nlp.pipeline)


#自定义流程

'''根本上来讲，一个流程组件就是一个函数或者callable，它读取一个doc，修改 和返回这个doc，作为下一个流程组件的输入。

要让spaCy找到我们的定制组件并调用，我们需要用@Language.component装饰器来装饰这个组件。 只需要将其放在函数定义的前一行即可。

一旦组件被注册后，我们就可以用nlp.add_pipe来将其加入到流程中。 这个方法需要至少一个参数:组件的字符串名。'''
from spacy.language import Language

@Language.component("custom_component") #custom_component为流程名
def custom_component_function(doc):
    # 对doc做一些处理
    return doc

nlp.add_pipe("custom_component")
'''last	如果为True则加在最后面	nlp.add_pipe("component", last=True)
first	如果为True则加在最前面	nlp.add_pipe("component", first=True)
before	加在指定组件之前	nlp.add_pipe("component", before="ner")
after	加在指定组件之后	nlp.add_pipe("component", after="tagger")
'''







#来一个简单的组件示例！

# 创建nlp实例
nlp = spacy.load("zh_core_web_sm")

# 定义一个定制化组件
@Language.component("custom_component")
def custom_component_function(doc):
    # 打印doc的长度
    print("Doc length:", len(doc))
    # 返回doc
    return doc

# 把组件添加到流程的最前面
nlp.add_pipe("custom_component", first=True)

# 打印流程的组件名
print("Pipeline:", nlp.pipe_names)
#现在可以看见我们已经在流程前面添加了自定义的组件~！

doc = nlp("这是一个句子。")#实例化一个 运行看看输出！