import json
import annotate
import os
from constant import *
from utils import *


def __match_keyword(keyword_list, word_list) -> list:
    result = []
    for keyword in keyword_list:
        for word in word_list:
            if keyword in word_list:
                result.append(word)
    return result


if __name__ == '__main__':
    log = init_logging()
    log.info('start main')

    with open(DIR_WORD_COUNT + FILE_NAME_MANUAL_REFINE) as f:
        keyword_dict = json.load(f)

    count_file = 0
    for root, ds, fs in os.walk(DIR_EXAMPLE):
        for fn in fs:
            dialogue_file = DIR_EXAMPLE + fn
            rewrite_file = DIR_REWRITE + fn
            with open(dialogue_file) as f:
                content = json.load(f)
            for turn in content:
                type_ = get_value_safe(turn, KEY_DIA_TYPE)
                speaker = get_value_safe(turn, KEY_DIA_SPEAKER)
                utterance = get_value_safe(turn, KEY_DIA_UTTERANCE)
                image_list = get_value_safe(utterance, KEY_DIA_IMAGES)
                text = get_value_safe(utterance, KEY_DIA_NLG)
                if text is None:
                    # log.warning('TEXT IS NONE: {}'.format(str(turn)))
                    continue
                text = text.lower()
                word_list = annotate.extract_words(text)
                result_num = annotate.extract_number(text)
                result_index = annotate.extract_index(text)

                current_result = dict()
                # for key_com in LIST_KEY_COM:
                #     current_result[key_com] = list()
                # for key_self in LIST_KEY_SELF:
                #     current_result[key_self] = list()

                flag_index_used = False if not result_index else True

                if KEY_COM_COLOR in text:
                    match_result = __match_keyword(keyword_dict[KEY_COM_COLOR], word_list)
                    if match_result:
                        current_result[KEY_COM_COLOR] = match_result
                    elif result_index:
                        current_result[KEY_COM_COLOR] = result_index
                        flag_index_used = True
                    else:
                        log.warning('VALUE NOT FOUND: {} - {}'.format(KEY_COM_COLOR, text))

                if KEY_COM_MATERIAL in text:
                    match_result = __match_keyword(keyword_dict[KEY_COM_MATERIAL], word_list)
                    if match_result:
                        current_result[KEY_COM_MATERIAL] = match_result
                    elif result_index:
                        current_result[KEY_COM_MATERIAL] = result_index
                        flag_index_used = True
                    else:
                        log.warning('VALUE NOT FOUND: {} - {}'.format(KEY_COM_MATERIAL, text))

                if KEY_COM_STYLE in text:
                    match_result = __match_keyword(keyword_dict[KEY_COM_STYLE], word_list)
                    if match_result:
                        current_result[KEY_COM_STYLE] = match_result
                    elif result_index:
                        current_result[KEY_COM_STYLE] = result_index
                        flag_index_used = True
                    else:
                        log.warning('VALUE NOT FOUND: {} - {}'.format(KEY_COM_STYLE, text))

                if KEY_COM_TYPE in text:
                    match_result = __match_keyword(keyword_dict[KEY_COM_TYPE], word_list)
                    if match_result:
                        current_result[KEY_COM_TYPE] = match_result
                    elif result_index:
                        current_result[KEY_COM_TYPE] = result_index
                        flag_index_used = True
                    else:
                        log.warning('VALUE NOT FOUND: {} - {}'.format(KEY_COM_TYPE, text))

                count_number_used = 0
                if KEY_SELF_AGE in word_list:
                    if result_num:
                        current_result[KEY_SELF_AGE] = result_num
                        count_number_used += 1
                    else:
                        log.warning('NUM NOT FOUND: {}'.format(text))

                if 'old' in word_list:
                    if result_num:
                        current_result[KEY_SELF_AGE] = result_num
                        count_number_used += 1
                    else:
                        log.warning('NUM NOT FOUND: {}'.format(text))

                if KEY_SELF_PRICE in text:
                    if result_num:
                        current_result[KEY_SELF_PRICE] = result_num
                        count_number_used += 1
                    elif result_index:
                        current_result[KEY_SELF_PRICE] = result_index
                        flag_index_used = True
                    else:
                        log.warning('VALUE NOT FOUND: {} - {}'.format(KEY_SELF_PRICE, text))

                if KEY_SELF_SIZE in text:
                    if result_num:
                        current_result[KEY_SELF_SIZE] = result_num
                        count_number_used += 1
                    elif result_index:
                        current_result[KEY_SELF_SIZE] = result_index
                        flag_index_used = True
                    else:
                        log.warning('VALUE NOT FOUND: {} - {}'.format(KEY_SELF_SIZE, text))

                # if not flag_index_used:
                #     log.warning('INDEX NOT USED: {}'.format(text))

                if result_num and count_number_used == 0:
                    log.warning('NUM NOT USED: {}'.format(text))

                if count_number_used > 1:
                    log.warning('NUM MULTI-USED: {}'.format(text))

                turn[KEY_DIA_STATE] = current_result

            with open(rewrite_file, 'w') as f:
                json.dump(content, f)
            count_file += 1
            if count_file % 1000 == 0:
                log.info('processed {:d} file'.format(count_file))

    log.info('finish main')
