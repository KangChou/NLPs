# pyhanlp句法训练

![image](https://user-images.githubusercontent.com/36963108/169463356-d2faf6c3-557d-49f4-83d7-235ec657c5b3.png)


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

