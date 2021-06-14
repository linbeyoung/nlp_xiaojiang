# -*- coding: utf-8 -*-
# @Time   : 2021/6/15 02:27
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : augmenttext_nlp.py

from AugmentText.augment_eda.enhance_eda import eda

def eda_nlp(input_file, aug_file):
    with open (input_file, 'r') as input:
        lines = input.readlines()

    for line in lines:
        aug_line = line.split('\t')
        sen = aug_line[0]
        label = aug_line[1]
        with open(aug_file, 'a') as output:
            output.write(sen + '\t' + label)
        sen_new_list = eda(sen)
        for sen_new in sen_new_list:
            print(sen_new + '\t' + label)
            with open(aug_file, 'a') as output:
                output.write(sen_new + '\t' + label)

input_file = '/Users/Beyoung/Desktop/Projects/nlp_cls/datasets/test.txt'
aug_file = '/Users/Beyoung/Desktop/Projects/nlp_cls/datasets/aug_data/test.txt'

eda_nlp(input_file, aug_file)