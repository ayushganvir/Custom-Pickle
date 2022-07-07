from pserial.lexer import lexical
from pserial.parser import parse
import math


serialized_file_loc = 'serialized_file.bin'


def serialize(dictionary):
    str_dict = _to_string(dictionary)
    val = _string_to_binary_list(str_dict)
    with open(serialized_file_loc, 'wb') as f:
        for char in val:
            s = str(char) + '\n'
            bt = s.encode()
            f.write(bt)


def deserialize():
    bin_list = []
    with open(serialized_file_loc, 'r') as f:
        for line in f:
            x = line[:-1]
            try:
                bin_list.append(int(x))
            except ValueError:
                print("Invalid File, Please Check.")

        return _from_string(_binary_to_string_list(bin_list))


def _from_string(string):
    tokens = lexical(string)
    return parse(tokens, is_root=True)[0]


def _to_string(json):
    json_type = type(json)
    if json_type is dict:
        string = '{'
        dict_len = len(json)

        for i, (key, val) in enumerate(json.items()):
            string += '"{}": {}'.format(key, _to_string(val))

            if i < dict_len - 1:
                string += ', '
            else:
                string += '}'

        return string
    elif json_type is list:
        string = '['
        list_len = len(json)

        for i, val in enumerate(json):
            string += _to_string(val)

            if i < list_len - 1:
                string += ', '
            else:
                string += ']'

        return string
    elif json_type is str:
        return '"{}"'.format(json)
    elif json_type is bool:
        return 'true' if json else 'false'
    elif json_type is None:
        return 'null'

    return str(json)


def _binary_to_string_list(a):
    l = []
    m = ""
    for i in a:
        b = 0
        c = 0
        k = int(math.log10(i)) + 1
        for j in range(k):
            b = ((i % 10) * (2 ** j))
            i = i // 10
            c = c + b
        l.append(c)
    for x in l:
        m = m + chr(x)
    return m


def _string_to_binary_list(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


