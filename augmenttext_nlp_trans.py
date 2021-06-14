# -*- coding: utf-8 -*-
# @Time   : 2021/6/15 02:27
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : augmenttext_nlp.py
from AugmentText.augment_translate.translate_web.translate_google import any_to_any_translate_back, GoogleToken, language_short_google

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

def trans_nlp(input_file, aug_file):
    with open (input_file, 'r') as input:
        lines = input.readlines()

    for line in lines:
        aug_line = line.split('\t')
        sen = aug_line[0]
        label = aug_line[1]
        with open(aug_file, 'a') as output:
            output.write(sen + '\t' + label)
        google_tokn = GoogleToken()
        for language_short_google_one in language_short_google:
            sen_new = any_to_any_translate_back(sen, from_='zh', to_=language_short_google_one)
            # judge = judge_translate_english(sen_org, text_translate)
            # if judge:
            #     print(language_short_google_one + " " + "True")
            print(text_translate.encode('utf-8', 'ignore').decode('utf-8') + '\t' + label)
            # else:
            #     print(language_short_google_one + " " + "False")
            #     print(text_translate.encode('gbk', 'ignore').decode('gbk'))
        # sen_new_list = eda(sen)
        # for sen_new in sen_new_list:
        #     print(sen_new + '\t' + label)
        #     with open(aug_file, 'a') as output:
        #         output.write(sen_new + '\t' + label)


        # sen_org = "过路蜻蜓喜欢口袋巧克力，这是什么意思"






if __name__ == '__main__':
    google_tokn = GoogleToken()
    # while True:
    sen_org = "过路蜻蜓喜欢口袋巧克力，这是什么意思"

    input_file = '/Users/Beyoung/Desktop/Projects/nlp_cls/datasets/train.txt'
    aug_file = '/Users/Beyoung/Desktop/Projects/nlp_cls/datasets/aug_data_trans/train.txt'

    # trans_nlp(input_file, aug_file)


    for language_short_google_one in language_short_google:
        text_translate = any_to_any_translate_back(sen_org, from_='zh', to_=language_short_google_one)
        # judge = judge_translate_english(sen_org, text_translate)
        # if judge:
        #     print(language_short_google_one + " " + "True")
        print(text_translate.encode('UTF-8', 'ignore').decode('UTF-8'))
        # else:
        #     print(language_short_google_one + " " + "False")
        #     print(text_translate.encode('gbk', 'ignore').decode('gbk'))