def get_value_safe(dic: dict, key):
    if dic is None:
        return None
    if key in dic.keys():
        return dic[key]
    return None
