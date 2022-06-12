import pandas as pd
import jieba as jb
import re
import tensorflow as tf
print(tf.__version__)
from sklearn.model_selection import train_test_split

# ck:https://codeantenna.com/a/vW7qeMbvDD
# 定义删除除字母,数字，汉字以外的所有符号的函数
def remove_punctuation(line):
    line = str(line)
    if line.strip() == '':
        return ''
    rule = re.compile(u"[^a-zA-Z0-9\u4E00-\u9FA5]")
    line = rule.sub('', line)
    return line

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def input_datasets(dfs,StopWords_path):
    # 加载停用词 :https://github.com/stopwords-iso/stopwords-zh
    stopwords = stopwordslist(StopWords_path)
    print("停用词:",stopwords)

    # 中文停用词包含了很多日常使用频率很高的常用词,如 吧，吗，呢，啥等一些感叹词等,这些高频常用词无法反应出文本的主要意思,所以要被过滤掉。
    dfs['clean_review'] = dfs['review'].apply(remove_punctuation)
    print(dfs.sample(10))

    """
    过滤掉了review中的标点符号和一些特殊符号，并生成了一个新的字段 clean_review。
    接下来我们要在clean_review的基础上进行分词,把每个评论内容分成由空格隔开的一个一个单独的词语。
    """
    # 分词，并过滤停用词
    dfs['cut_review'] = dfs['clean_review'].apply(lambda x: " ".join([w for w in list(jb.cut(x)) if w not in stopwords]))
    # print("分词，并过滤停用词:",df.head())

    print("处理结果:",dfs)
    """
    数据集中拆分出训练集和验证集,我们将80%的数据作为训练集,20%的数据作为验证集，我们通过分层抽样的方式来随机抽样，
    注意在这里我们使用了sklearn的train_test_split的方法来抽样,并使用了stratify参数来保证抽样后,
    训练集和验证集中的各个类目的占比与原数据集保持一致。
    """
    X_train, X_validation, Y_train, Y_validation = train_test_split(dfs[['cut_review']], dfs[["cat"]], test_size=0.2,
                                                                    stratify=dfs.cat)
    return X_train, X_validation, Y_train, Y_validation,dfs

def output_datasets():
    # https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/online_shopping_10_cats/online_shopping_10_cats.zip
    df = pd.read_csv('./datasets/online_shopping_10_cats.csv')
    print("数据总量: %d ." % len(df))
    # print(df.sample(10),df)
    # print(df["review"][0])
    print("总共有多少个类目：", df[["cat"]].drop_duplicates().reset_index(drop=True))

    print("---------各个类目的数据量以及占比-------------")
    print(df.cat.value_counts())
    print(df.cat.value_counts() / len(df))

    # 获取指定标签类别的数据
    print(df[df.cat == '平板'][["review"]].sample(5).values)

    StopWords_path="./datasets/chineseStopWords.txt"
    return input_datasets(df,StopWords_path)







