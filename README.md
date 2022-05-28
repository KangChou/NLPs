

# NLPs
Deep learning speech learning library




# 数据集

中文、英文NER、英汉机器翻译数据集。中英文实体识别数据集，中英文机器翻译数据集，中文分词数据集：https://github.com/quincyliang/nlp-public-dataset

CTB词性标注集

![image](https://user-images.githubusercontent.com/36963108/170655243-6267fbc4-246d-40f0-8303-7c97a934918a.png)

![image](https://user-images.githubusercontent.com/36963108/170656452-738fbb77-03bc-4315-a3fb-d14a50a9b5f6.png)

ck: https://help.aliyun.com/document_detail/179146.html?scm=20140722.184.2.173

标注标签说明：https://verbs.colorado.edu/chinese/segguide.3rd.ch.pdf

https://blog.csdn.net/qq_40332976/article/details/120331450


# 资料汇总

一个轻量级、简单易用的 RNN 唤醒词监听器: [https://github.com/MycroftAI/mycroft-precise](https://github.com/MycroftAI/mycroft-precise)

zh:[http://fancyerii.github.io/books/mycroft-precise/](http://fancyerii.github.io/books/mycroft-precise/)

基于树莓派的人工智能小车，实现识别、提示、智能旅游线路、离线图像:
[https://github.com/dalinzhangzdl/AI_Car_Raspberry-pi](https://github.com/dalinzhangzdl/AI_Car_Raspberry-pi)

中文NLP数据集:[https://github.com/CLUEbenchmark/CLUEDatasetSearch](https://github.com/CLUEbenchmark/CLUEDatasetSearch) 

模型：[https://github.com/CLUEbenchmark/CLUE](https://github.com/CLUEbenchmark/CLUE) 

中文 NLP 资源精选列表 中文自然语言处理相关资料:
[https://github.com/crownpku/Awesome-Chinese-NLP](https://github.com/crownpku/Awesome-Chinese-NLP)

视觉聊天机器人:[https://paperswithcode.com/paper/visual-dialog](https://paperswithcode.com/paper/visual-dialog)

Bert/Transformer模型压缩与优化加速: https://blog.csdn.net/nature553863/article/details/120292394：

可以压缩 BERT 的所有方式：http://mitchgordon.me/machine/learning/2019/11/18/all-the-ways-to-compress-BERT.html
https://www.leiphone.com/category/academic/MkV1j604LvPt1wcx.html

BERT轻量化探索—模型剪枝（BERT Pruning）—Rasa维度剪枝:https://blog.csdn.net/ai_1046067944/article/details/103609152 

压缩 BERT 以加快预测速度:https://rasa.com/blog/compressing-bert-for-faster-prediction-2/

论文综述与BERT相关最新论文:[https://github.com/tomohideshibata/BERT-related-papers](https://github.com/tomohideshibata/BERT-related-papers)

中文自然语言排行榜及论文查询:[https://www.cluebenchmarks.com/index.html](https://www.cluebenchmarks.com/index.html)

计算语言学国际会议论文集:[https://aclanthology.org/volumes/2020.coling-main/](https://aclanthology.org/volumes/2020.coling-main/)

计算语言学协会第 58 届年会论文集:https://aclanthology.org/volumes/2020.acl-main/

计算语言学2协会2021年会论文搜集：https://aclanthology.org/events/acl-2021/

中文BERT全词掩蔽预训练（中文BERT-wwm系列模型）[https://github.com/ymcui/Chinese-BERT-wwm](https://github.com/ymcui/Chinese-BERT-wwm)

一个大规模的中文跨领域面向任务的对话数据集:[https://github.com/thu-coai/CrossWOZ](https://github.com/thu-coai/CrossWOZ)

关于ConvLab-2：用于构建、评估和诊断对话系统的开源工具包（支持中文）：[https://github.com/thu-coai/ConvLab-2](https://github.com/thu-coai/ConvLab-2)

视觉和语言预训练模型 (VL-PTM) 的最新进展(语音视觉融合):[https://github.com/yuewang-cuhk/awesome-vision-language-pretraining-papers](https://github.com/yuewang-cuhk/awesome-vision-language-pretraining-papers)

深度学习和自然语言处理阅读清单:[https://github.com/IsaacChanghau/DL-NLP-Readings](https://github.com/IsaacChanghau/DL-NLP-Readings)

视觉问答 (VQA)（图像/视频问答）、视觉问题生成、视觉对话、视觉常识推理和相关领域的精选列表：[https://github.com/jokieleung/awesome-visual-question-answering](https://github.com/jokieleung/awesome-visual-question-answering)

汇总得不错的nlp学习资料:https://jackkuo666.github.io/ 

dl4nlp自然语言处理深度学习课程材料:https://github.com/liu-nlp/dl4nlp

HanLP的Python接口，支持自动下载与升级HanLP，兼容py2、py3。内部算法经过工业界和学术界考验，配套书籍《自然语言处理入门》已经出版，欢迎查阅随书代码:https://github.com/jiajunhua/hankcs-pyhanlp/tree/3fc9c7d8a3f5eae00988db743c44b7708520b5f1

# pyhanlp文本训练与预测API接口
```python
from pyhanlp import *
from tests.test_utility import ensure_data

IClassifier = JClass('com.hankcs.hanlp.classification.classifiers.IClassifier')
NaiveBayesClassifier = JClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')
# 中文情感挖掘语料-ChnSentiCorp 数据来自：
chn_senti_corp = ensure_data("ChnSentiCorp情感分析酒店评论", "http://file.hankcs.com/corpus/ChnSentiCorp.zip")


def predict(classifier, text):
    print("《%s》 情感极性是 【%s】" % (text, classifier.classify(text)))


if __name__ == '__main__':
    classifier = NaiveBayesClassifier()
    #  创建分类器，更高级的功能请参考IClassifier的接口定义
    classifier.train(chn_senti_corp)
    #  训练后的模型支持持久化，下次就不必训练了
    predict(classifier, "前台客房服务态度非常好！早餐很丰富，房价很干净。再接再厉！")
    predict(classifier, "结果大失所望，灯光昏暗，空间极其狭小，床垫质量恶劣，房间还伴着一股霉味。")
    predict(classifier, "可利用文本分类实现情感分析，效果不是不行")

```

