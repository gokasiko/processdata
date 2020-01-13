import os
import sys
import json
import pickle
import pandas as pd

sys.path.append('..')
from freebase.graph import KnowledgeGraph


def collect_subject_set(smart_result_file, *webqsp_file):
    el_data = pd.read_csv(smart_result_file, header=None, sep='\t')
    subject_set = set()
    ent_mid_list = el_data[4]
    for ent_mid in ent_mid_list:
        subject_set.add(ent_mid.strip('/').replace('/', '.'))

    for file in webqsp_file:
        sp_data = json.load(open(file, 'r', encoding='utf-8'))
        for q in sp_data['Questions']:
            for p in q['Parses']:
                ent_mid = p['TopicEntityMid']
                subject_set.add(ent_mid)
    return subject_set



def extract_first_hop_triple(freebase_file, subgraph_file, subject_set):
    fout = open(subgraph_file, 'w', encoding='utf-8')
    with open(freebase_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            s, p, o, _ = line.rstrip('\n').split('\t')
            fb_prefix = 'http://rdf.freebase.com/ns/'
            if s.find(fb_prefix) == -1 or p.find(fb_prefix) == -1:
                continue
            s = s[s.rfind('/') + 1: len(s) - 1]
            if s in subject_set:
                fout.write(line)


def collect_mid_set(one_hop_triple_file):
    mid_set = set()
    with open(one_hop_triple_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            s, p, o, _ = line.rstrip('\n').split('\t')
            fb_prefix = 'http://rdf.freebase.com/ns/'
            if s.find(fb_prefix) == -1 or p.find(fb_prefix) == -1 or o.find(fb_prefix) == -1:
                continue
            o = o[o.rfind('/') + 1: len(o) - 1]
            mid_set.add(o)
    return mid_set


def extract_second_hop_triple(freebase_file, subgraph_file, mid_set):
    fout = open(subgraph_file, 'w', encoding='utf-8')
    with open(freebase_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            s, p, o, _ = line.rstrip('\n').split('\t')
            fb_prefix = 'http://rdf.freebase.com/ns/'
            if s.find(fb_prefix) == -1 or p.find(fb_prefix) == -1:
                continue
            s = s[s.rfind('/') + 1: len(s) - 1]
            if s in mid_set:
                fout.write(line)

def generate_subgraph(first_hop_triples, second_hop_triples, save_path):
    fout = open(save_path, 'w', encoding='utf-8')
    with open(first_hop_triples, 'r', encoding='utf-8') as fin:
        for line in fin:
            fout.write(line)
    with open(second_hop_triples, 'r', encoding='utf-8') as fin:
        for line in fin:
            fout.write(line)


def get_one_hop_cand_dict(first_hop_triples_file, rel_pool):
    one_hop_cand_dict = {}
    rel_dict = {rel: idx for idx, rel in enumerate(rel_pool)}
    with open(first_hop_triples_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            s, p, o, _ = line.rstrip('\n').split('\t')
            fb_prefix = 'http://rdf.freebase.com/ns/'
            if s.find(fb_prefix) == -1 or p.find(fb_prefix) == -1:
                continue
            s = s[s.rfind('/') + 1: len(s) - 1]
            p = p[p.rfind('/') + 1: len(p) - 1]
            if p in rel_pool:
                if s not in one_hop_cand_dict:
                    one_hop_cand_dict[s] = set()
                one_hop_cand_dict[s].add(rel_dict[p])
    result = {}
    for key, value in one_hop_cand_dict.items():
        result[key] = ' '.join([str(x) for x in value])
    return result


def split_rel_pool(rel_pool):
    first_rel_pool = set()
    second_rel_pool = set()
    for rels in rel_pool:
        if rels.find('..') == -1:
            continue
        rels = rels.split('..')
        first_rel_pool.add(rels[0])
        second_rel_pool.add(rels[1])
    return first_rel_pool, second_rel_pool


def get_second_rel_triples(second_rel_pool):
    fout = open('./new_second_hop_triples.WebQSP.ttl', 'w', encoding='utf-8')
    with open('./second_hop_triples.WebQSP.ttl', 'r', encoding='utf-8') as fin:
        for line in fin:
            s, p, o, _ = line.rstrip('\n').split('\t')
            fb_prefix = 'http://rdf.freebase.com/ns/'
            if s.find(fb_prefix) == -1 or p.find(fb_prefix) == -1:
                continue
            p = p[p.rfind('/') + 1: len(p) - 1]
            if p in second_rel_pool:
                fout.write(line)

def get_cand_dict(subject_set, kg, rel_pool):
    rel_pool = set(rel_pool)
    cand_dict = {}
    rel_dict = {rel: idx for idx, rel in enumerate(rel_pool)}

    for idx, sub in enumerate(subject_set):
        rel_list = kg.ret_all_out_rels(sub)
        cand_dict[sub] = []
        for rel in rel_list:
            if rel in rel_pool:
                cand_dict[sub].append(rel_dict[rel])
        print(idx, len(cand_dict[sub]))
    result = {}
    for key, value in cand_dict.items():
        result[key] = ' '.join([str(x) for x in value])
    return result


if __name__ == '__main__':
    # subject_set = collect_subject_set('../data/S-MART/webquestions.examples.test.e2e.top10.filter.tsv',
    #                                   '../data/WebQSP/data/WebQSP.train.json',
    #                                   '../data/WebQSP/data/WebQSP.test.json')
    # json.dump(list(subject_set), open('WebQSP.entity.subject.json', 'w', encoding='utf-8'), indent=2)
    # print('Extract unary relations begins.')
    # extract_first_hop_triple('/home/test/dataset/freebase-rdf-20171026.ttl', './first_hop_triples.WebQSP.ttl', subject_set)
    # print('Extract unary relations ends.')

    # mid_set = collect_mid_set('./first_hop_triples.WebQSP.ttl')
    # json.dump(list(mid_set), open('./cvt.node.WebQSP.json', 'w', encoding='utf-8'), indent=2)
    #
    # extract_second_hop_triple('/home/test/dataset/freebase-rdf-20171026.ttl', './second_hop_triples.WebQSP.ttl', mid_set)


    # rel_pool = pickle.load(open('../transformer/rel.pool.pkl', 'rb'))
    # print(rel_pool)
    # one_hop_cand_dict = get_one_hop_cand_dict('./first_hop_triples.WebQSP.ttl', rel_pool)
    # json.dump(one_hop_cand_dict, open('./one_hop_cand.json', 'w', encoding='utf-8'), indent=2)

    # f_rel_pool, s_rel_pool = split_rel_pool(rel_pool)
    # print(list(s_rel_pool))
    # print(len(s_rel_pool))
    # get_second_rel_triples(s_rel_pool)

    # generate_subgraph('./first_hop_triples.WebQSP.ttl', './new_second_hop_triples.WebQSP.ttl', './subgraph.WebQSP.ttl')

    # kg = KnowledgeGraph()
    # print('loading knowledge graph ...')
    # kg.load('./subgraph.WebQSP.ttl')
    # print('loading completed.\nentity size: %d\nrelation size: %d\n' % (kg.get_ent_size(), kg.get_rel_size()))
    #
    # subject_set = json.load(open('./WebQSP.entity.subject.json'))
    #
    # cand_dict = get_cand_dict(subject_set, kg, rel_pool)
    # json.dump(cand_dict, open('WebQSP.cand.rels.json', 'w', encoding='utf-8'), indent=2)

    with open('/home/test/dataset/freebase-rdf-20171026.ttl', 'r', encoding='utf-8') as fin:
        for line in fin:
            s, p, o, _ = line.rstrip('\n').split('\t')
            fb_prefix = 'http://rdf.freebase.com/ns/'
            if s.find(fb_prefix) == -1 or p.find(fb_prefix) == -1:
                continue
            s = s[s.rfind('/') + 1: len(s) - 1]
            p = p[p.rfind('/') + 1: len(p) - 1]
            if p != 'type.object.name':
                continue
            if s == 'm.02dtg' or s == 'm.01p5_w':
                print(s, p, o)
