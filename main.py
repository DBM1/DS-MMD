import json
import annotate
import os
from constant import *
from utils import *

if __name__ == '__main__':
    with open(FILE_NAME_MANUAL_REFINE) as f:
        keyword_dict = json.load(f)

    for root, ds, fs in os.walk(DIR_EXAMPLE):
        for fn in fs:
            dialogue_file = DIR_EXAMPLE + fn
            with open(dialogue_file) as f:
                content = json.load(f)
            for turn in content:
                type_ = get_value_safe(turn, KEY_DIA_TYPE)
                speaker = get_value_safe(turn, KEY_DIA_SPEAKER)
                utterance = get_value_safe(turn, KEY_DIA_UTTERANCE)
                image_list = get_value_safe(utterance, KEY_DIA_IMAGES)
                text = get_value_safe(utterance, KEY_DIA_NLG)
                result_num = annotate.extract_number(text)
                current_result = dict()







                if result_num:
                    for keyword in LIST_SLOT_KEYWORD:
                        pass
