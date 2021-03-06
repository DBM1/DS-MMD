import json
import annotate
import os
from collections import Counter
from constant import *
from utils import *


def __word_counter(word_list: list, top_n=10):
    if word_list:
        counter = Counter(word_list)
        return counter.most_common(top_n)
    return None


if __name__ == '__main__':
    log = init_logging()
    log.info('start processing')

    value_statistic = dict()
    for key_com in LIST_KEY_COM:
        value_statistic[key_com] = list()

    for root, ds, fs in os.walk(DIR_COM_AMAZON):
        for fn in fs:
            commodity_file = DIR_COM_AMAZON + fn
            with open(commodity_file) as f:
                content = json.load(f)
                for key_com in LIST_KEY_COM:
                    value = get_value_safe(content, key_com)
                    if value and value not in value_statistic[key_com]:
                        word_list = annotate.extract_words(value)
                        if key_com == KEY_COM_COLOR:
                            word_list = [word for word in word_list if len(word) > 2]
                        if key_com == KEY_COM_TYPE:
                            word_list = [word for word in word_list if len(word) > 2]
                        if key_com == KEY_COM_STYLE:
                            word_list = [word for word in word_list if len(word) > 3]
                        if key_com == KEY_COM_GENDER:
                            pass
                        if key_com == KEY_COM_MATERIAL:
                            word_list = [word for word in word_list if len(word) > 3]
                        value_statistic[key_com] += word_list
    log.info('finish json analyzing')

    for key_com in LIST_KEY_COM:
        log.info('start {} counting'.format(key_com))
        tuple_list = __word_counter(value_statistic[key_com], None)
        count_dict = tuple_list_to_dict(tuple_list)
        statistic_file = DIR_WORD_COUNT + key_com + FILE_SUFFIX_JSON
        with open(statistic_file, 'w') as f:
            json.dump(count_dict, f)
        log.info('finish {} counting'.format(key_com))
