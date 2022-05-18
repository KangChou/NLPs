
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

jiba分词demo:
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


```python

spacy+jieba实现分词：
```
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






# 参考：补充

安装指定版本：
```
# pip uninstall zh_core_web_trf zh_core_web_sm zh_core_web_md
# pip install thinc==7.1.1 srsly ujson regex cytoolz spacy==2.2 preshed==3.0.2
```
