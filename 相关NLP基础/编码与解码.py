


jan="教会は初めてですか"
chi="请问是第一次来到教会吗"


def simplesplit(str):   #简单分词
    list=[]
    for word in str:
        list.append(word)
    return list

input = simplesplit(jan)
output = simplesplit(chi)

print(input)
print(output)


