import logging


def get_value_safe(dic: dict, key):
    if dic is None:
        return None
    if key in dic.keys():
        return dic[key]
    return None


def get_values(dic: dict, key_list: list) -> dict:
    pass


def tuple_list_to_dict(tuple_list: list) -> dict:
    result = dict()
    if tuple_list:
        for tuple_ in tuple_list:
            result[tuple_[0]] = tuple_[1]
    return result


def init_logging():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO)
    return logging
