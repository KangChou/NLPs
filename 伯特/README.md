

https://github.com/search?q=bert

BERT的官方代码Y阅读参考：http://fancyerii.github.io/2019/03/09/bert-codes/

Transformer代码阅读： http://fancyerii.github.io/2019/03/09/transformer-codes/

图解Transformer：http://fancyerii.github.io/2019/03/09/transformer-illustrated/


讲的不错的文章：https://zhuanlan.zhihu.com/p/394780960
```
生成训练样本:create_pretraining_data.py
原始样本
切词 tokenization
创建样本实例
保存为tfrecord

python create_pretraining_data.py \
  --input_file=./sample_text.txt \
  --output_file=/tmp/tf_examples.tfrecord \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --do_lower_case=True \
  --max_seq_length=128 \
  --max_predictions_per_seq=20 \
  --masked_lm_prob=0.15 \
  --random_seed=12345 \
  --dupe_factor=5

-训练模型
构建模型：modeling.py
构建优化器：optimization.py
训练模型：run_pretraining.py

fine tune
分类：run_classifier.py
tf_hub使用：run_classifier_with_tfhub.py
问答：run_squad.py
句子向量表示：extract_features.py

```

日志记录：
```
global_step/sec：一个性能指标，显示我们在模型训练时每秒处理了多少批次（梯度更新）
global_step/sec：显示我们在进行模型训练时每秒处理的批次数（梯度更新）。其中global_step（全局步数）用于指数衰减学习率。


global_step/sec = 0.204125
表示每秒训练多少个batch批次；

examples/sec = 3.26599
表示每秒可以训练的样本数量 ；

Num examples = 40127
表示样本的总数量

Batch size = 16
表示一批次有多少个样本；

Num steps = 25079
表示总共有多少步（批次）

Epoch = 10
迭代次数，即所有样本训练的次数

Epoch = Num steps * Batch size / Num examples
      = 25079 * 16 / 40127
	  = 10 次


Num steps = Num examples * Epoch / Batch size
25079 = 40127 * 10 / 16

一个迭代训练用时 = Num examples / (examples/sec)
                 = 40127 / 3.26599
				 = 12286秒
				 = 3小时 24分 46秒

训练总用时(秒) = Num examples * Epoch / (examples/sec) (秒)
               = 40127 * 10 / 3.26599
		       = 122863 秒
		       = 34小时 7分 43秒

或者:
训练总用时(秒) = Num steps  / (global_step/sec) (秒)
               = 25079 / 0.204125
			   = 122861 秒
		       = 34小时 7分 41秒

** 附带一个时间长度的转换方法，可用于把秒数变成时间长度 **：
```
```
# 经过的秒数 转成 时间长度
测试样例：
>>> getSpanTimes(122891234,unit='')
'3Y 10M 22D 08:27:14;'
>>> getSpanTimes(122891234,unit='en')
'3 Years 10 Months 22 Days 08 Hour 27 Minute 14 Second'
>>> getSpanTimes(122891234,unit='zh')
'3年 10个月 22天 08小时 27分 14秒'

def getSpanTimes (lngTimeSpan, unit=''):
    import time
    unit_sim = 'Y |M |D |:|:|;'
    unit_en = ' Years | Months | Days | Hour | Minute | Second'
    unit_zh = '年 |个月 |天 |小时 |分 |秒'
    if unit=='en':
        unit_list = unit_en.split('|')
    elif unit=='zh':
        unit_list = unit_zh.split('|')
    else:
        unit_list = unit_sim.split('|')
    t = time.gmtime(float(round(lngTimeSpan,3)))
    #print(t)
    total_time = ''
    total_time += ('%d%s'  % (t.tm_year-1970, unit_list[0])) if t.tm_year>1970 else ''
    total_time += ('%d%s' % (t.tm_mon-1, unit_list[1])) if t.tm_mon>1 else ''
    total_time += ('%d%s'   % (t.tm_mday-1, unit_list[2])) if t.tm_mday>1 else ''
    tm = "%%H%s%%M%s%%S%s" % tuple(unit_list[3:])
    total_time += time.strftime(tm, t)
    return total_time

```
