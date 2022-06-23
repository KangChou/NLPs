import numpy as np
np.random.seed(0)       # to reproduce experimental results
from tqdm import tqdm
import codecs
import argparse
from scipy import spatial
import os

def gen_data(ref_path, cand_path, cand_size, output_parth, if_reverse=False):
    with codecs.open(ref_path, 'r','utf-8') as ref_fr, codecs.open(cand_path, 'r', 'utf-8') as cand_fr, codecs.open(output_parth, 'w', 'utf-8') as fw:
        lines = ref_fr.readlines()
        id_1_2_map = {}
        for line in lines:
            info = line.split("\t")
            if if_reverse:
                id_1 = int(info[1])
                id_2 = int(info[0])
            else:
                id_1 = int(info[0])
                id_2 = int(info[1])
            id_1_2_map[id_1] = id_2

        lines = cand_fr.readlines()
        for line in lines:
            info = line.strip().split(":")
            id_1 = int(info[0])
            gold_id_2 = id_1_2_map[id_1]
            cands = info[1].strip().split(" ")
            cands = cands[:cand_size]
            for cand in cands:
                cand = int(cand)
                label = 0
                if cand == gold_id_2:
                    label = 1
                fw.write(str(id_1) + "\t" + str(cand) + "\t" + str(label)+"\n")

def gen_graph(triple_path, feature_path):
    fw_graph, bw_graph = build_graph(triple_path)
    features = extract_node_feature(feature_path)
    id_list = list(features.keys())
    features_list, adj_list = extract_sub_graph(id_list, features, fw_graph)
    res_map = {}
    for _ in range(len(id_list)):
        id = id_list[_]
        feature = features_list[_]
        adj = adj_list[_]
        jo = {}
        jo['g_ids_features'] = feature
        jo['g_adj'] = adj
        res_map[id] = jo
    return res_map


def extract_sub_graph(id_list, id_features, fw_graph):
    g_ids_features_list = []
    g_adj_list = []
    for _ in tqdm(range(len(id_list))):
        id = id_list[_]
        g_ids_features = {}
        g_adj = {}
        id_mapping = {}
        hop_1_ids = [id]

        if id in fw_graph:
            fw_neighbor_info = fw_graph[id]
            for (rel_id, obj_id) in fw_neighbor_info:
                if obj_id not in hop_1_ids:
                    hop_1_ids.append(obj_id)

        # if type == "full":
        #     if id in bw_graph:
        #         bw_neighbor_info = bw_graph[id]
        #         for (rel_id, subj_id) in bw_neighbor_info:
        #             if subj_id not in hop_1_ids:
        #                 hop_1_ids.append(subj_id)

        for subj_id in hop_1_ids:
            if subj_id not in id_mapping:
                id_mapping[subj_id] = len(id_mapping)

            subj_mapped_id = id_mapping[subj_id]

            if subj_mapped_id not in g_ids_features:
                feature = id_features[subj_id]
                g_ids_features[subj_mapped_id] = feature

            if subj_mapped_id not in g_adj:
                g_adj[subj_mapped_id] = []

            if subj_id in fw_graph:
                fw_neighbor_info = fw_graph[subj_id]
                for (rel_id, obj_id) in fw_neighbor_info:
                    if obj_id not in hop_1_ids: continue

                    if obj_id not in id_mapping:
                        id_mapping[obj_id] = len(id_mapping)
                    obj_mapped_id = id_mapping[obj_id]

                    if obj_mapped_id not in g_adj[subj_mapped_id]:
                        g_adj[subj_mapped_id].append(obj_mapped_id)

                    if obj_mapped_id not in g_ids_features:
                        feature = id_features[obj_id]
                        g_ids_features[obj_mapped_id] = feature

        g_ids_features_list.append(g_ids_features)
        g_adj_list.append(g_adj)

    return g_ids_features_list, g_adj_list

def neg_sampling(refs, node_1_ids, node_2_ids):
    examples = []
    for _ in range(len(refs)):
        np.random.shuffle(node_1_ids)
        np.random.shuffle(node_2_ids)

        info = refs[_].split("\t")
        id_1 = int(info[0])
        id_2 = int(info[1])

        id_1_negs = []
        id_2_negs = []

        for __ in range(5):
            if node_1_ids[__] != id_1:
                id_1_negs.append(int(node_1_ids[__]))
            if node_2_ids[__] != id_2:
                id_2_negs.append(int(node_2_ids[__]))

        # we generate five training examples for each positive pair
        examples.append((id_1, id_2, 1))
        for __ in range(2):
            examples.append((id_1_negs[__], id_2, 0))
            examples.append((id_1, id_2_negs[__], 0))

    return examples

def extract_node_feature(feature_path):
    with codecs.open(feature_path, 'r', 'utf-8') as f:
        res = {}
        lines = f.readlines()
        for line in lines:
            info = line.strip().split('\t')
            id = int(info[0])
            if len(info) != 2:
                feature = "**UNK**"
            else:
                feature = info[1].lower()
            res[id] = feature
        return res

def build_graph(triple_file_path):
    with codecs.open(triple_file_path, 'r', 'utf-8') as f:
        fw_graph = {}
        bw_graph = {}
        lines = f.readlines()
        for line in lines:
            info = line.strip().split("\t")
            subj_id = int(info[0])
            rel_id = int(info[1])
            obj_id = int(info[2])

            if subj_id not in fw_graph:
                fw_graph[subj_id] = []
            fw_graph[subj_id].append((rel_id, obj_id))

            if obj_id not in bw_graph:
                bw_graph[obj_id] = []
            bw_graph[obj_id].append((rel_id, subj_id))

        return fw_graph, bw_graph

# def show_example_graph(id, triple_path, id_feature_path):
#     fw_graph, bw_graph = build_graph(triple_path)
#     node_features = extract_node_feature(id_feature_path)
#
#     id_list = [id]
#     g_ids_features_list, g_adj_list = extract_sub_graph(id_list, node_features, fw_graph)
#     g_adj = g_adj_list[0]
#     g_ids_features = g_ids_features_list[0]
#
#     print("topic entity id is {}".format(id))
#     for adj_ori_id in fw_graph[id]:
#         print(adj_ori_id)
#
#     for id in g_adj:
#         adj_ids = g_adj[id]
#         print(str(id)+"\t"+g_ids_features[id])
#         for adj_id in adj_ids:
#             print("\t"+str(adj_id)+"\t"+g_ids_features[adj_id])

def cand_gen(ref_path, id_features_1_path, id_features_2_path, pre_trained_emb_path, cand_list_path, cand_size):
    def if_zero_vec(vec):
        tag = True
        for _ in range(len(vec)):
            if vec[_] != 0.0:
                tag = False
                break
        return tag

    with codecs.open(ref_path, 'r', 'utf-8') as f, \
            codecs.open(pre_trained_emb_path, 'r', 'utf-8') as emb_fr, \
            codecs.open(id_features_1_path, 'r', 'utf-8') as feature_1_f, \
            codecs.open(id_features_2_path, 'r', 'utf-8') as feature_2_f, \
            codecs.open(cand_list_path, 'w', 'utf-8') as cand_list_fw:
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
    argparser = argparse.ArgumentParser()
    argparser.add_argument("type", type=str)
    argparser.add_argument("mode", type=str, choices=["train", "test", "dev"])
    argparser.add_argument("cand_size", type=int)
    args = argparser.parse_args()
    mode = args.mode
    cand_size = args.cand_size
    problem_type = args.type

    triple_1_path = problem_type + "/triples_1"
    triple_2_path = problem_type + "/triples_2"
    ref_ent_ids = problem_type + "/ref_ent_ids"
    id_features_1 = problem_type + "/id_features_1"
    id_features_2 = problem_type + "/id_features_2"
    pre_trained_emb_path = "sub.glove.300d"

    if mode == "train":
        train_ref_path = problem_type + "/train.ref"
        train_cand_path = problem_type + "/train.cand_list." + str(cand_size)
        train_data_path = problem_type + "/train.examples." + str(cand_size)
        if os.path.exists(train_cand_path):
            print("candidate file for training is ready ...")
        else:
            print("generating candidate file for training ...")
            cand_gen(train_ref_path, id_features_1, id_features_2, pre_trained_emb_path, train_cand_path, cand_size)
        print("generating training data for graph matching model...")
        gen_data(train_ref_path, train_cand_path, cand_size, train_data_path)

    elif mode == "test":
        test_ref_path = problem_type + "/test.ref"
        test_cand_path = problem_type + "/test.cand_list." + str(cand_size)
        test_data_path = problem_type + "/test.examples." + str(cand_size)
        if os.path.exists(test_cand_path):
            print("candidate file for test is ready ...")
        else:
            print("generating candidate file for test ...")
            cand_gen(test_ref_path, id_features_1, id_features_2, pre_trained_emb_path, test_cand_path, cand_size)
        print("generating test data for graph matching model...")
        gen_data(test_ref_path, test_cand_path, cand_size, test_data_path)

    elif mode == "dev":
        dev_ref_path = problem_type + "/test.ref"
        test_cand_path = problem_type + "/test.cand_list." + str(cand_size)   # we use test candidate list to construct the dev data
        dev_data_path = problem_type + "/dev.examples.20"
        if os.path.exists(test_cand_path):
            print("candidate file for dev is ready ...")
        else:
            print("generating candidate file for dev...")
            cand_gen(dev_ref_path, id_features_1, id_features_2, pre_trained_emb_path, test_cand_path, cand_size)
        print("generating dev data for graph matching model...")
        gen_data(dev_ref_path, test_cand_path, 20, dev_data_path)
