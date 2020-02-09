import argparse
import atexit
import csv
import datetime
import glob
import json
import os
import sys
import codecs

field_map = {
    'payee':'被给付方',
    'payer':'给付方',
    'fyPayer':'承担方'
}

#no usage here
def build_wenshu(wenshu_data, folder_path):
    with codecs.open(wenshu_data, 'r') as fin:
        reader = csv.reader(fin)
        for item in reader:
            if reader.line_num == 1:
                continue
            tmp_path = os.path.join(folder_path, item[14]+'.bin')
            with codecs.open(tmp_path, 'w') as fout:
                fout.write(item[4])

def gen_extraction_report(extract_result_path, ground_truth_path):
    ground_truth = {}
    total = 0
    predict = 0
    correct = 0
    with codecs.open(ground_truth_path, 'r') as fin:
        reader = csv.reader(fin)
        for item in reader:
            if reader.line_num == 1:
                continue
            file_name = item[1].split("/")[-1].split('.')[0]
            if file_name not in ground_truth:
                ground_truth[file_name] = []
                print("Add file:{}".format(file_name))
            try:
                tmp_truth = field_map[item[3]]+'|'+item[4]+'|'+item[5]+'|'+item[7]+'|'+item[8]
            except IndexError:
                print(file_name)
            ground_truth[file_name].append(tmp_truth)
            total += 1

    with codecs.open(extract_result_path, 'r') as fin:
        reader = csv.reader(fin)
        for item in reader:
            file_name = item[0].split("/")[-1].split('.')[0]
            if file_name not in ground_truth:
                # print("This file not in ground truth: {}".format(file_name))
                continue
            else:
                tmp_truth = '|'.join(item[2:7])
                if tmp_truth in ground_truth[file_name]:
                    print("Correct: {} {}".format(file_name, tmp_truth))
                    correct += 1
                else:
                    print("Wrong: {} {}".format(file_name, tmp_truth))

            predict += 1
    pre = correct/predict
    rec = correct/total
    print("Total: {} Prec: {} Recall: {} F1: {}".format(total, pre, rec, 2*pre*rec/(pre+rec)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--analyze_data', type=str, default='data/final_result.csv')
    parser.add_argument('--build_wenshu_path', type=str, default='input/wenshu_100')
    parser.add_argument('--extract_result_path', type=str, default='output/output.csv')
    parser.add_argument('--ground_truth_path', type=str, default='data/analyse_answer2.csv')
    ns = parser.parse_args()

    # build_wenshu(ns.analyze_data, ns.build_wenshu_path)
    gen_extraction_report(ns.extract_result_path, ns.ground_truth_path)



