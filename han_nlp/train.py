# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-02-11 23:18
# 《自然语言处理入门》12.5.1 训练模型
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/

from pyhanlp import *
import zipfile
import os

from pyhanlp.static import download, remove_file, HANLP_DATA_PATH


def test_data_path():
    """
    获取测试数据路径，位于$root/data/test，根目录由配置文件指定。
    :return:
    """
    data_path = os.path.join(HANLP_DATA_PATH, 'test')
    if not os.path.isdir(data_path):
        os.mkdir(data_path)
    return data_path


def ensure_data(data_name, data_url):
    root_path = test_data_path()
    dest_path = os.path.join(root_path, data_name)
    if os.path.exists(dest_path):
        return dest_path
    if data_url.endswith('.zip'):
        dest_path += '.zip'
    download(data_url, dest_path)
    if data_url.endswith('.zip'):
        with zipfile.ZipFile(dest_path, "r") as archive:
            archive.extractall(root_path)
        remove_file(dest_path)
        dest_path = dest_path[:-len('.zip')]
    return dest_path

KBeamArcEagerDependencyParser = JClass('com.hankcs.hanlp.dependency.perceptron.parser.KBeamArcEagerDependencyParser')
CTB_ROOT = ensure_data("ctb8.0-dep", "http://file.hankcs.com/corpus/ctb8.0-dep.zip")
CTB_TRAIN = CTB_ROOT + "/train.conll"#训练集
CTB_DEV = CTB_ROOT + "/dev.conll" # 开发集
CTB_TEST = CTB_ROOT + "/test.conll" # 词聚类问件
CTB_MODEL = CTB_ROOT + "/ctb.bin" # 模型
BROWN_CLUSTER = ensure_data("wiki-cn-cluster.txt", "http://file.hankcs.com/corpus/wiki-cn-cluster.zip")

if __name__ == '__main__':
    parser = KBeamArcEagerDependencyParser.train(CTB_TRAIN, CTB_DEV, BROWN_CLUSTER, CTB_MODEL)
    print(parser.parse("人吃鱼"))
    score = parser.evaluate(CTB_TEST)
    print("UAS=%.1f LAS=%.1f\n" % (score[0], score[1]))
    # 参考：https://www.cnblogs.com/qiu-hua/articles/12235764.html
    # 模型生成路径：/opt/conda/lib/python3.6/site-packages/pyhanlp/data
