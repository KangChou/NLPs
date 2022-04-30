
# 文本标注

## 1、脚本标注
中文分词、词性标注、实体识别的工具整理；相关数据集整理与预处理；通用评测脚本脚本。

参考来自：https://github.com/Bond-H/lac_tools_benchment

安装与使用介绍，整理包括以下工具：

https://github.com/Bond-H/lac_tools_benchment/blob/master/lac_tools.md

```shell
LAC
Jieba
THULAC
pkuseg
pyhanlp
StandfordNLP
LTP
SnowNLP
PyNLPIR
foolnltk
```

## 2、命名实体识别的三种标注方法

1.BMES（四位序列标注法）
```shell
B表示一个词的词首位值，M表示一个词的中间位置，E表示一个词的末尾位置，S表示一个单独的字词。
我/S 是/S 中/B 国/M 人/E
我/是/中国人/ (标注上分出来的实体块)
```

2.BIO（三位序列标注法）
```shell
B-begin,I-inside,O-outside
B-X代表实体X的开头
I-X代表实体的结尾
O代表不属于任何类型的
```

3.BIOES（四位序列标注法）
```shell
B-begin，I-inside，O-outside，E-end，S-single
B表示开始
I表示内部
O表示非实体
E实体尾部
S表示该词本身就是一个实体
```
