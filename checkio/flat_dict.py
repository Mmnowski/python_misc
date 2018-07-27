def flatten(dictionary):
    ret_dict = {}
    ret_key = ''
    ret_value = ''

    for key, value in dictionary.items():
        ret_key = key
        if type(value) == dict:
            if len(value) != 0:
                for sub_key, sub_value in value.items():
                    ret_value = sub_value
                    ret_dict[ret_key+'/'+sub_key] = ret_value
            else:
                ret_value = ""
                ret_dict[ret_key] = ret_value
        else:
            ret_dict[key] = value
    for n in ret_dict.values():
        if type(n) == dict:
            ret_dict = flatten(ret_dict)
    return ret_dict


if __name__ == '__main__':
    # test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    # print(' Input: {}'.format(test_input))
    # print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
