# pyhanlp句法训练

![image](https://user-images.githubusercontent.com/36963108/169463356-d2faf6c3-557d-49f4-83d7-235ec657c5b3.png)
```bash
python train.py 
下载 http://file.hankcs.com/corpus/ctb8.0-dep.zip 到 /opt/conda/lib/python3.6/site-packages/pyhanlp/static/data/test/ctb8.0-dep.zip
100%   3.5 MiB 114.3 KiB/s ETA:  0 s [=============================================================]
下载 http://file.hankcs.com/corpus/wiki-cn-cluster.zip 到 /opt/conda/lib/python3.6/site-packages/pyhanlp/static/data/test/wiki-cn-cluster.txt.zip
100% 763.9 KiB 353.9 KiB/s ETA:  0 s [=============================================================]
训练集句子数量: 14863                                                                               
迭代 1/20 100.00%  耗时 544 秒。UAS=83.23 LAS=80.84 最高分！保存中...
迭代 2/20 100.00%  耗时 569 秒。UAS=84.06 LAS=81.97 最高分！保存中...
迭代 3/20 100.00%  耗时 557 秒。UAS=84.55 LAS=82.48 最高分！保存中...
迭代 4/20 100.00%  耗时 556 秒。UAS=84.82 LAS=82.74 最高分！保存中...
迭代 5/20 100.00%  耗时 553 秒。UAS=84.95 LAS=82.89 最高分！保存中...
迭代 6/20 100.00%  耗时 549 秒。UAS=85.18 LAS=83.15 最高分！保存中...
迭代 7/20 100.00%  耗时 560 秒。UAS=85.25 LAS=83.26 最高分！保存中...
迭代 8/20 100.00%  耗时 562 秒。UAS=85.12 LAS=83.11
迭代 9/20 100.00%  耗时 569 秒。UAS=85.23 LAS=83.24
迭代 10/20 100.00%  耗时 571 秒。UAS=85.17 LAS=83.23
迭代 11/20 100.00%  耗时 571 秒。UAS=85.20 LAS=83.22
迭代 12/20 100.00%  耗时 581 秒。UAS=85.09 LAS=83.16
迭代 13/20 100.00%  耗时 652 秒。UAS=85.16 LAS=83.24
迭代 14/20 100.00%  耗时 677 秒。UAS=85.21 LAS=83.26
迭代 15/20 100.00%  耗时 586 秒。UAS=85.24 LAS=83.31
迭代 16/20 100.00%  耗时 554 秒。UAS=85.26 LAS=83.33 最高分！保存中...
迭代 17/20 100.00%  耗时 537 秒。UAS=85.38 LAS=83.46 最高分！保存中...
迭代 18/20 100.00%  耗时 548 秒。UAS=85.43 LAS=83.49 最高分！保存中...
迭代 19/20 100.00%  耗时 553 秒。UAS=85.39 LAS=83.43
迭代 20/20 100.00%  耗时 554 秒。UAS=85.41 LAS=83.46
1       人      人      N       NN      _       2       nsubj   _       _
2       吃      吃      V       VV      _       0       ROOT    _       _
3       鱼      鱼      N       NN      _       2       dobj    _       _

100 ... 200 ... 300 ... 400 ... 500 ... 600 ... 700 ... 800 ... 900 ... 1000 ... 1100 ... 1200 ... 1300 ... 1400 ... 1500 ... 1600 ... 1700 ... 1800 ... 1900 ... UAS=85.4 LAS=83.5
```

# spacy句法

句法是指句子的各个组成部分的相互关系，句法分析分为句法结构分析（syntactic structure parsing）和依存关系分析(dependency parsing)。句法结构分析用于获取整个句子的句法结构，依存分析用于获取词汇之间的依存关系，目前的句法分析已经从句法结构分析转向依存句法分析。

依存语法通过分析语言单位内成分之间的依存关系揭示其句法结构，主张句子中核心动词是支配其它成分的中心成分，而它本身却不受其它任何成分的支配，所有受支配成分都以某种依存关系从属于支配者。

在20世纪70年代，Robinson提出依存语法中关于依存关系的四条公理：

- 一个句子中只有一个成分是独立的；
- 其它成分直接依存于某一成分；
- 任何一个成分都不能依存与两个或两个以上的成分；
- 如果A成分直接依存于B成分，而C成分在句中位于A和B之间，那么C或者直接依存于B，或者直接依存于A和B之间的某一成分；

SpaCy 中文模型:https://github.com/howl-anderson/Chinese_models_for_SpaCy \
https://blog.csdn.net/lllhhhv/article/details/123335675 \
zh_core_web_trf、zh_core_web_md 等,它们的区别在于准确度和体积大小, zh_core_web_sm 体积小,准确度相比zh_core_web_trf差,zh_core_web_trf相对就体积大。这样可以适应不同场景.


# 数据参考
hanlp.pretrained.dep。CTB5_BIAFFINE_DEP_ZH= 'https://file.hankcs.com/hanlp/dep/biaffine_ctb5_20191229_025833.zip'
在 CTB5 上训练的Biaffine LSTM 模型（Dozat & Manning 2017）。

hanlp.pretrained.dep。CTB7_BIAFFINE_DEP_ZH= 'https://file.hankcs.com/hanlp/dep/biaffine_ctb7_20200109_022431.zip'
在 CTB7 上训练的Biaffine LSTM 模型（Dozat & Manning 2017）。

hanlp.pretrained.dep。CTB9_DEP_ELECTRA_SMALL= 'https://file.hankcs.com/hanlp/dep/ctb9_dep_electra_small_20220216_100306.zip'
Electra 小型编码器 ( Clark et al. 2020 ) 和 Biaffine 解码器 ( Dozat & Manning 2017 ) 在 CTB9-SD330 上训练。性能为 UAS=87.68% LAS=83.54%。

hanlp.pretrained.dep。CTB9_UDC_ELECTRA_SMALL= 'https://file.hankcs.com/hanlp/dep/udc_dep_electra_small_20220218_095452.zip'
Electra 小型编码器 ( Clark et al. 2020 ) 和 Biaffine 解码器 ( Dozat & Manning 2017 ) 在 CTB9-UD420 上训练。性能是 UAS=85.92% LAS=81.13% 。

hanlp.pretrained.dep。PMT1_DEP_ELECTRA_SMALL= 'https://file.hankcs.com/hanlp/dep/pmt_dep_electra_small_20220218_134518.zip'
Electra 小型编码器 ( Clark et al. 2020 ) 和 Biaffine 解码器 ( Dozat & Manning 2017 ) 在 PKU Multi-view Chinese Treebank (PMT) 1.0 ( Qiu et al. 2014 ) 上训练。性能是 UAS=91.21% LAS=88.65%。

hanlp.pretrained.dep。PTB_BIAFFINE_DEP_EN= 'https://file.hankcs.com/hanlp/dep/ptb_dep_biaffine_20200101_174624.zip'
在 PTB 上训练的Biaffine LSTM 模型（Dozat & Manning 2017 ）。

参考来自：https://hanlp.hankcs.com/docs/api/hanlp/index.html

