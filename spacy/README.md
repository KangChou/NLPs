
# spacy中文预训练模型使用
env:
```
UBUNTU 16.04
PYTHON 3.6+anaconda3

```
  
## 安装
```
pip install spacy==3.3.0
pip install jieba==0.42.1
# python -m spacy download zh_core_web_sm
# python -m spacy download zh_core_web_md
# python -m spacy download zh_core_web_lg
# python -m spacy download zh_core_web_trf
# python -m spacy download zh_core_web_trf -i  https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com
```

## jiba分词demo
```python
import jieba
text = "我喜欢北京的秋天。"
print("all search")
print(jieba.lcut(text,cut_all=True))
# # 或者：
print([i for i in jieba.cut(text,cut_all=True)])

# print("accurate search")
print(jieba.lcut(text,cut_all=False))
# # 或者：
print([i for i in jieba.cut(text,cut_all=False)])

# print("search_for_engineer")
print(jieba.lcut_for_search(text))
# # 或者：
print([i for i in jieba.cut_for_search(text)])

```

输出结果：

```bash
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 0.428 seconds.
Prefix dict has been built successfully.
['我', '喜欢', '北京', '的', '秋天', '。']
['我', '喜欢', '北京', '的', '秋天', '。']
['我', '喜欢', '北京', '的', '秋天', '。']
['我', '喜欢', '北京', '的', '秋天', '。']
['我', '喜欢', '北京', '的', '秋天', '。']
['我', '喜欢', '北京', '的', '秋天', '。']


```

## spacy+jieba实现分词
```python
import spacy
spacy_zh = spacy.load("zh_core_web_sm")
text = "我喜欢北京的秋天。"
def tokenize_zh(text):
    return [tok.text for tok in spacy_zh.tokenizer(text)]
print(tokenize_zh(text))

```
输出结果：
```
['我', '喜欢', '北京', '的', '秋天', '。']

````
## 依存句法

```python
import spacy
parser = spacy.load('zh_core_web_sm')
 
doc = parser('小明在上海虹口足球场观看足球比赛。')
for token in doc[:17]:
    print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\n".format(
        token.text,   # 文本
        token.idx,  # 索引值（即在原文中的定位）
        token.lemma_,  # 词元(lemma)
        token.head,   # 当前Token的Parent Token，从语法关系上来看，每一个Token都只有一个Head。
        token.dep_, # 依存关系
        token.children, # 语法上的直接子节点
        token.ancestors, # 语法上的父节点
        token.is_punct, # 是否为标点符号
        token.is_space,  # 是否为空格
        token.shape_,  # 字个数用x表示，如：两个字就是xx
        token.pos_,  # 词性
        token.tag_  # 标记
    ))

```

![image](https://user-images.githubusercontent.com/36963108/168963178-642d28d3-7ce5-4bc6-a55e-32c39c21a2b9.png)

其他参考：SpaCy中文  https://github.com/howl-anderson/Chinese_models_for_SpaCy 

![image](https://user-images.githubusercontent.com/36963108/168965425-b83914ed-7614-4cad-928b-8ad7e04ca2cf.png)



# 参考：补充

安装指定版本：
```
# pip uninstall zh_core_web_trf zh_core_web_sm zh_core_web_md
# pip install thinc==7.1.1 srsly ujson regex cytoolz spacy==2.2 preshed==3.0.2
```
spaCy V3.0 文本分类模型训练、评估、打包及数据预处理：https://blog.csdn.net/u014607067/article/details/115294589

spaCy的方法进行训练一个新的招投标实体标注模型：https://blog.csdn.net/weixin_45965387/article/details/124140084

实体识别spacy训练模型和更新：https://blog.csdn.net/qq_35385687/article/details/119793624

spacy从头开始训练一个词性标注模型:https://blog.csdn.net/weixin_44711529/article/details/116331270
```
TRAIN_DATA = [
    ("我喜欢红苹果味道", {'tags': ['N', 'V', 'J', 'N','P']}),
    ("吃蓝色汉堡味道很好", {'tags': ['V', 'J', 'N','P','J']}),
    ("黄色香蕉味道很甜", {'tags': ['J', 'N', 'P','J']}),
    ("羊肉肉质味道很好", {'tags': ['N', 'N', 'P','J']}),
    ("她喜欢闻香水味道", {'tags': ['N', 'N', 'V','N','P']})
]

```
spacy-zh:https://github.com/middle-plat-ai/spacy_zh_model    https://www.jianshu.com/u/3b77f85cc918

https://github.com/jeusgao/spaCy-new-language-test-Chinese

nlp-base:https://github.com/JackKuo666/Python_nlp_notes

