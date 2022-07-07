from .constants import *

JSON_QUOTE = '"'
JSON_WHITESPACE = [' ', '\t', '\b', '\n', '\r']
JSON_SYNTAX = [JSON_COMMA, JSON_COLON, JSON_LEFTBRACKET, JSON_RIGHTBRACKET,
               JSON_LEFTBRACE, JSON_RIGHTBRACE]

LEN_FALSE = len('false')
LEN_TRUE = len('true')
LEN_NULL = len('null')


def lexical_string(string):
    json_string = ''

    if string[0] == JSON_QUOTE:
        string = string[1:]
    else:
        return None, string

    for c in string:
        if c == JSON_QUOTE:
            return json_string, string[len(json_string) + 1:]
        else:
            json_string += c

    raise Exception('Expected end-of-string quote')


def lexical_number(string):
    json_number = ''

    number_characters = [str(d) for d in range(0, 10)] + ['-', 'e', '.']

    for c in string:
        if c in number_characters:
            json_number += c
        else:
            break

    rest = string[len(json_number):]

    if not len(json_number):
        return None, string

    if '.' in json_number:
        return float(json_number), rest

    return int(json_number), rest


def lexical_bool(string):
    string_len = len(string)

    if string_len >= LEN_TRUE and \
            string[:LEN_TRUE] == 'true':
        return True, string[LEN_TRUE:]
    elif string_len >= LEN_FALSE and \
            string[:LEN_FALSE] == 'false':
        return False, string[LEN_FALSE:]

    return None, string


def lexical_null(string):
    string_len = len(string)

    if string_len >= LEN_NULL and \
            string[:LEN_NULL] == 'null':
        return True, string[LEN_NULL]

    return None, string


def lexical(string):
    tokens = []

    while len(string):
        json_string, string = lexical_string(string)
        if json_string is not None:
            tokens.append(json_string)
            continue

        json_number, string = lexical_number(string)
        if json_number is not None:
            tokens.append(json_number)
            continue

        json_bool, string = lexical_bool(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue

        json_null, string = lexical_null(string)
        if json_null is not None:
            tokens.append(None)
            continue

        c = string[0]

        if c in JSON_WHITESPACE:
            # Ignore whitespace
            string = string[1:]
        elif c in JSON_SYNTAX:
            tokens.append(c)
            string = string[1:]
        else:
            raise Exception('Unexpected character: {}'.format(c))

    return tokens
