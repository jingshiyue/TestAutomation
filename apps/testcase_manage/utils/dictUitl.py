def dict_in(dict1: dict, dict2: dict):
    """
    判断前面的字典是否在后面字典之中
    :param dict1: 字典
    :param dict2: 字典
    :return: bool
    """
    for k in dict1:
        if k in dict2:
            v1 = dict1.get(k)
            v2 = dict2.get(k)
            if isinstance(v1, dict):
                return dict_in(v1, v2)
            else:
                return v1 == v2
        else:
            return False
    return False


if __name__ == '__main__':
    a1 = {'message': 'OK'}
    a2 = {'phone': '18780373592', 'realname': '完美'}
    a3 = {'data': {'phone': '18780373592', 'realname': '完美'}}
    b = {'message': 'OK', 'data': {'phone': '18780373592', 'realname': '完美', "haha": 123}}
    print(dict_in(a1, b))
    print(dict_in(a2, b))
    print(dict_in(a3, b))
