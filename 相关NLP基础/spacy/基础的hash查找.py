import spacy



nlp = spacy.blank('zh')

nlp.vocab.strings.add('咖啡')
#查找指定string的哈希值
coffee_hash=nlp.vocab.strings['咖啡'] #vocab存储多文档共享数据;所有字符串被spacy编码为hash值
#根据hash值查找字符串
coffee_string=nlp.vocab.strings[coffee_hash]


print(coffee_hash,coffee_string)