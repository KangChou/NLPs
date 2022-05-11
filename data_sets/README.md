# 中文依存句法树库

目前最有名的开源自由的依存树库当属UD ( Universal Dependencies)，它以“署名-非商业性使用-相同方式共享4.0”等类似协议免费向公众授权。UD是个跨语种的语法标注项目，一共有 200 多名贡献者为 70 多种语言标注了 100 多个树库。具体到中文，存在4个不同领域的树库。本章选取其中规模最大的 UD_ Chinese GSD 作为示例。该树库的语种为繁体中文，将其转换为简体中文后，供大家下载使用。

http://file.hankcs.com/corpus/chs-gsd-ud.zip

该树库的格式为 CoNLL-U，这是一种以制表符分隔的表格格式。CoNLL-U 文件有10列，每行都是一个单词， 空白行表示句子结束。单元中的下划线 _ 表示空白， 结合其中一句样例，解释如表所示。

![image](https://user-images.githubusercontent.com/36963108/167612786-87b67139-f42f-4a23-a772-295321353845.png)


词性标注集合依存关系标注集请参考 UD 的官方网站:

http://niversaldependencies.org/guidelines.html

另一份著名的语料库依然是 CTB，只不过需要额外利用一些工具将短语结构树转换为依存句法树。读者可以直接下载转换后的 CTB 依存句法树库，其格式是类似于 CoNLl-U 的 CoNLL。

依存句法树的可视化

工具如下:

南京大学汤光超开发的 Dependency Viewer。导入 .conll 扩展名的树库文件即可。
brat 标注工具。
可视化工具可以帮助我们理解句法树的结构，比较句子之间的不同。

