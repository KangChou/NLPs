

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

