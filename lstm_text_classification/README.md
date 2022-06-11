# lstm文本情感分析
（Sentiment Analysis）

情感极性（倾向）分析。所谓情感极性分析，指的是对文本进行褒义、贬义、中性的判断。在大多应用场景下，只分为两类。
例如对于“喜爱”和“厌恶”这两个词，就属于不同的情感倾向。


![image](https://user-images.githubusercontent.com/36963108/173188980-ac618f90-6146-4419-ae08-9152aa28f66c.png)



TextClassification/data/data_single.csv 该数据集一共有4310条评论数据，文本的情感分为两类：“正面”和“反面”


数据集的前几行如下：
```buildoutcfg
evaluation,label
用了一段时间，感觉还不错，可以,正面
电视非常好，已经是家里的第二台了。第一天下单，第二天就到本地了，可是物流的人说车坏了，一直催，客服也帮着催，到第三天下午5点才送过来。父母年纪大了，买个大电视画面清晰，趁着耳朵还好使，享受几年。,正面
电视比想象中的大好多，画面也很清晰，系统很智能，更多功能还在摸索中,正面
不错,正面
```
![image](https://user-images.githubusercontent.com/36963108/173188724-b8c5b456-9c56-4f5e-a56b-a28e2681ef4b.png)

```buildoutcfg
# 设置matplotlib绘图时的字体
my_font = font_manager.FontProperties(fname="./Songti.ttc")
Songti.ttc字体库下载地址：https://drive.google.com/drive/folders/1iZqrFBJPGkpCIFsVuQwcmAdqBZGdOZnB
```
# References:

```buildoutcfg
https://github.com/DA1YAYUAN/JD-comments-sentiment-analysis
https://github.com/renjunxiang/Text-Classification
https://www.cnblogs.com/jclian91/p/10886031.html
https://www.mscto.com/q/129589514267000832
```
