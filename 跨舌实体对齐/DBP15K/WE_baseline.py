from scipy import spatial
from tqdm import tqdm
import codecs
import argparse

def if_zero_vec(vec):
    tag = True
    for _ in range(len(vec)):
        if vec[_] != 0.0:
            tag = False
            break
    return tag

def evl(test_ref_path, id_features_1_path, id_features_2_path, pre_trained_emb_path, cand_list_path, cand_size, if_reverse=False):
    with codecs.open(test_ref_path, 'r', 'utf-8') as f, codecs.open(pre_trained_emb_path, 'r', 'utf-8') as emb_fr, codecs.open(id_features_1_path, 'r', 'utf-8') as feature_1_f, codecs.open(id_features_2_path, 'r', 'utf-8') as feature_2_f, codecs.open(cand_list_path+"."+str(cand_size), 'w', 'utf-8') as cand_list_fw:
        w_vec = {}
        lines = emb_fr.readlines()
        for line in lines:
            info = line.strip().split(" ")
            w = info[0]
            vec = [float(x) for x in info[1:]]
            w_vec[w] = vec

        # ============ retrieve each node's representation in graph 1 ==================
        id_1_vec = {}
        zero_vec_id1 = set()
        lines = feature_1_f.readlines()
        for line in lines:
            info = line.strip().split("\t")
            id = int(info[0])

            vec = [0.0 for _ in range(300)]
            if len(info) > 1:
                for w in info[1].split(' '):
                    w = w.lower()
                    if w in w_vec:
                        v = w_vec[w]
                        vec = [vec[_] + v[_] for _ in range(300)]
            vec = [vec[_] for _ in range(300)]
            id_1_vec[id] = vec

            if if_zero_vec(vec):
                zero_vec_id1.add(id)

        # ============ retrieve each node's representation in graph 2 ==================
        id_2_vec = {}
        zero_vec_id2 = set()
        lines = feature_2_f.readlines()
        for line in lines:
            info = line.strip().split("\t")
            id = int(info[0])

            vec = [0.0 for _ in range(300)]
            if len(info) > 1:
                for w in info[1].split(' '):
                    w = w.lower()
                    if w in w_vec:
                        v = w_vec[w]
                        vec = [vec[_] + v[_] for _ in range(300)]
            vec = [vec[_] for _ in range(300)]
            id_2_vec[id] = vec

            if if_zero_vec(vec):
                zero_vec_id2.add(id)

        # ========================= calculate the acc #1 and acc # 10 and record the results =========================
        lines = f.readlines()
        correct_1 = 0.0
        correct_10 = 0.0
        correct_most = 0.0
        count = 0.0
        for _ in tqdm(range(len(lines))):
            line = lines[_]
            info = line.strip().split("\t")
            if if_reverse:
                id_1 = int(info[1])
                id_2 = int(info[0])
            else:
                id_1 = int(info[0])
                id_2 = int(info[1])

            vec_1 = id_1_vec[id_1]

            if id_1 not in zero_vec_id1:
                count += 1.0
                cand_id_2_score_map = {}
                for id_2_cand in id_2_vec.keys():
                    if id_2_cand in zero_vec_id2: continue
                    cos_sim = 1 - spatial.distance.cosine(vec_1, id_2_vec[id_2_cand])
                    cand_id_2_score_map[id_2_cand] = cos_sim

                cand_id_2_score_items = cand_id_2_score_map.items()
                cand_id_2_score_items = sorted(cand_id_2_score_items, key=lambda d: d[1], reverse=True)

                cand_list_fw.write(str(id_1)+": ")
                for idx in range(cand_size):
                    if int(cand_id_2_score_items[idx][0]) == int(id_2):
                        if idx == 0:
                            correct_1 += 1.0
                        if idx < 10:
                            correct_10 += 1.0
                        if idx < cand_size:
                            correct_most += 1.0
                    cand_list_fw.write(str(cand_id_2_score_items[idx][0])+" ")
                cand_list_fw.write('\n')


    print("correct at #1 acc: {}".format(correct_1/count))
    print("correct at #10 acc: {}".format(correct_10/count))
    print("correct at #{} acc: {}".format(cand_size, correct_most/count))


if __name__ == "__main__":
    # dir = 'zh_en'
    # dirs = ['zh_en', 'fr_en', 'ja_en']
    # dirs = ['ja_en']
    # for dir in dirs:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("dir", type=str, choices=["zh_en", "fr_en", "ja_en", "en_zh", "en_fr", "en_ja"])
    argparser.add_argument("type", type=str, choices=["train", "test"])
    argparser.add_argument("cand_size", type=int)
    args = argparser.parse_args()
    cand_size = args.cand_size
    dir = args.dir
    type = args.type

    reverse = False
    if dir.startswith("en_"):
        reverse = True

    print("evaluating the baseline on {}".format(dir))

    if not reverse:
        evl(dir + '/'+type+'.ref', dir + '/id_features_1', dir + '/id_features_2', 'sub.glove.300d', dir+'/'+type+'.cand_list', cand_size)
    else:
        info = dir.split("_")
        phy_dir = info[1]+"_"+info[0]
        evl(phy_dir + '/' + type + ".ref", phy_dir + '/id_features_2', phy_dir + '/id_features_1', 'sub.glove.300d', phy_dir+'/'+dir + "."+ type+'.cand_list', cand_size, if_reverse=True)